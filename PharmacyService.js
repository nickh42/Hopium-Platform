import { haversineDistanceMeters } from '../models/Pharmacy';

/**
 * PharmacyService
 * Queries the Google Places API "Nearby Search" endpoint for pharmacies
 * close to the user's current location.
 *
 * NOTE: You must supply your own Google Places API key (see README.md /
 * GOOGLE_MAPS_API_KEY below). Without a key this will throw, and the UI
 * will show a friendly error state instead of crashing.
 */

// Replace with your own key, ideally injected via an environment variable
// (e.g. using react-native-dotenv or Expo's app.config.js `extra` field)
// rather than committed to source control.
const GOOGLE_PLACES_API_KEY = process.env.GOOGLE_PLACES_API_KEY || 'YOUR_GOOGLE_PLACES_API_KEY';

const NEARBY_SEARCH_URL = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json';

/**
 * Fetches pharmacies within `radiusMeters` of the given coordinates.
 * @param {{latitude: number, longitude: number}} coords
 * @param {number} radiusMeters
 * @returns {Promise<Array>} normalized pharmacy list, sorted by distance
 */
export async function fetchNearbyPharmacies(coords, radiusMeters = 5000) {
  if (!coords) throw new Error('Missing coordinates for pharmacy search.');

  const params = new URLSearchParams({
    location: `${coords.latitude},${coords.longitude}`,
    radius: String(radiusMeters),
    type: 'pharmacy',
    key: GOOGLE_PLACES_API_KEY,
  });

  const response = await fetch(`${NEARBY_SEARCH_URL}?${params.toString()}`);

  if (!response.ok) {
    throw new Error(`Places API request failed with status ${response.status}`);
  }

  const data = await response.json();

  if (data.status !== 'OK' && data.status !== 'ZERO_RESULTS') {
    throw new Error(`Places API error: ${data.status}`);
  }

  const results = data.results || [];

  return results
    .map((place) => {
      const lat = place.geometry?.location?.lat;
      const lng = place.geometry?.location?.lng;
      return {
        id: place.place_id,
        name: place.name,
        address: place.vicinity || 'Address unavailable',
        latitude: lat,
        longitude: lng,
        distanceMeters:
          lat != null && lng != null
            ? haversineDistanceMeters(coords.latitude, coords.longitude, lat, lng)
            : null,
        openNow: place.opening_hours?.open_now ?? null,
      };
    })
    .sort((a, b) => (a.distanceMeters ?? Infinity) - (b.distanceMeters ?? Infinity));
}

export default { fetchNearbyPharmacies };
