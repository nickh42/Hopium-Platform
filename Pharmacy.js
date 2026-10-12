/**
 * Pharmacy.js
 * Shape of a normalized Pharmacy object used throughout the app.
 * This is a plain JS "model" (JSDoc typedef) rather than a class, since the
 * app only ever reads pharmacy data returned by the Places API.
 *
 * @typedef {Object} Pharmacy
 * @property {string} id            - Unique place ID from the Places API.
 * @property {string} name          - Pharmacy name (e.g. "Walgreens").
 * @property {string} address       - Formatted street address.
 * @property {number} latitude
 * @property {number} longitude
 * @property {number|null} distanceMeters - Distance from the user, if known.
 * @property {boolean} openNow      - Whether the location is currently open, if known.
 */

/**
 * Calculates the straight-line distance between two lat/lng points using the
 * Haversine formula. Used to display an approximate distance to each pharmacy.
 * @returns {number} distance in meters
 */
export function haversineDistanceMeters(lat1, lon1, lat2, lon2) {
  const R = 6371000; // Earth radius in meters
  const toRad = (deg) => (deg * Math.PI) / 180;

  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);

  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLon / 2) * Math.sin(dLon / 2);

  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

export function formatDistance(meters) {
  if (meters == null) return '';
  if (meters < 1000) return `${Math.round(meters)} m away`;
  return `${(meters / 1000).toFixed(1)} km away`;
}
