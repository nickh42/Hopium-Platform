import * as Location from 'expo-location';

/**
 * LocationService
 * Wraps expo-location to request permissions and fetch the user's current
 * position, with clear status results the UI can branch on.
 */

export const LocationStatus = {
  GRANTED: 'GRANTED',
  DENIED: 'DENIED',
  UNAVAILABLE: 'UNAVAILABLE',
  ERROR: 'ERROR',
};

/**
 * Requests foreground location permission and returns the current position.
 * @returns {Promise<{status: string, coords: {latitude: number, longitude: number} | null}>}
 */
export async function getCurrentLocation() {
  try {
    const servicesEnabled = await Location.hasServicesEnabledAsync();
    if (!servicesEnabled) {
      return { status: LocationStatus.UNAVAILABLE, coords: null };
    }

    const { status } = await Location.requestForegroundPermissionsAsync();
    if (status !== 'granted') {
      return { status: LocationStatus.DENIED, coords: null };
    }

    const position = await Location.getCurrentPositionAsync({
      accuracy: Location.Accuracy.Balanced,
    });

    return {
      status: LocationStatus.GRANTED,
      coords: {
        latitude: position.coords.latitude,
        longitude: position.coords.longitude,
      },
    };
  } catch (error) {
    return { status: LocationStatus.ERROR, coords: null };
  }
}

export default { getCurrentLocation, LocationStatus };
