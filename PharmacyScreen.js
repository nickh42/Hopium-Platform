import React, { useEffect, useState, useCallback } from 'react';
import { View, Text, StyleSheet, SafeAreaView, Linking, Platform } from 'react-native';
import MapView, { Marker, Callout, PROVIDER_GOOGLE } from 'react-native-maps';
import { Ionicons } from '@expo/vector-icons';
import PrimaryButton from '../components/PrimaryButton';
import { colors, spacing, typography, radius } from '../utils/colors';
import { getCurrentLocation, LocationStatus } from '../services/LocationService';
import { fetchNearbyPharmacies } from '../services/PharmacyService';
import { formatDistance } from '../models/Pharmacy';

const SCREEN_STATE = {
  LOADING: 'LOADING',
  READY: 'READY',
  PERMISSION_DENIED: 'PERMISSION_DENIED',
  GPS_UNAVAILABLE: 'GPS_UNAVAILABLE',
  NO_RESULTS: 'NO_RESULTS',
  ERROR: 'ERROR',
};

export default function PharmacyScreen() {
  const [screenState, setScreenState] = useState(SCREEN_STATE.LOADING);
  const [userCoords, setUserCoords] = useState(null);
  const [pharmacies, setPharmacies] = useState([]);

  const loadPharmacies = useCallback(async () => {
    setScreenState(SCREEN_STATE.LOADING);

    const { status, coords } = await getCurrentLocation();

    if (status === LocationStatus.DENIED) {
      setScreenState(SCREEN_STATE.PERMISSION_DENIED);
      return;
    }
    if (status === LocationStatus.UNAVAILABLE) {
      setScreenState(SCREEN_STATE.GPS_UNAVAILABLE);
      return;
    }
    if (status === LocationStatus.ERROR || !coords) {
      setScreenState(SCREEN_STATE.ERROR);
      return;
    }

    setUserCoords(coords);

    try {
      const results = await fetchNearbyPharmacies(coords);
      setPharmacies(results);
      setScreenState(results.length === 0 ? SCREEN_STATE.NO_RESULTS : SCREEN_STATE.READY);
    } catch (error) {
      setScreenState(SCREEN_STATE.ERROR);
    }
  }, []);

  useEffect(() => {
    loadPharmacies();
  }, [loadPharmacies]);

  const openNavigation = (pharmacy) => {
    const query = encodeURIComponent(pharmacy.name);
    const url = Platform.select({
      ios: `maps://app?daddr=${pharmacy.latitude},${pharmacy.longitude}&q=${query}`,
      android: `google.navigation:q=${pharmacy.latitude},${pharmacy.longitude}`,
      default: `https://www.google.com/maps/dir/?api=1&destination=${pharmacy.latitude},${pharmacy.longitude}`,
    });
    Linking.openURL(url).catch(() => {
      // Fallback to web maps if the native app URL scheme fails
      Linking.openURL(
        `https://www.google.com/maps/dir/?api=1&destination=${pharmacy.latitude},${pharmacy.longitude}`
      );
    });
  };

  const openManualSearch = () => {
    Linking.openURL('https://www.google.com/maps/search/pharmacies+near+me');
  };

  if (screenState === SCREEN_STATE.LOADING) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.centered}>
          <Ionicons name="location" size={40} color={colors.primary} />
          <Text style={styles.messageTitle}>Finding nearby pharmacies&hellip;</Text>
        </View>
      </SafeAreaView>
    );
  }

  if (screenState === SCREEN_STATE.PERMISSION_DENIED) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.centered}>
          <Ionicons name="lock-closed" size={40} color={colors.textSecondary} />
          <Text style={styles.messageTitle}>Location access needed</Text>
          <Text style={styles.messageBody}>
            We use your location to find pharmacies near you. Please enable location permissions
            for this app in your device settings, or search manually below.
          </Text>
          <PrimaryButton label="Search Manually" variant="outline" onPress={openManualSearch} style={styles.actionButton} />
          <PrimaryButton label="Try Again" variant="primary" onPress={loadPharmacies} style={styles.actionButton} />
        </View>
      </SafeAreaView>
    );
  }

  if (screenState === SCREEN_STATE.GPS_UNAVAILABLE) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.centered}>
          <Ionicons name="navigate" size={40} color={colors.textSecondary} />
          <Text style={styles.messageTitle}>GPS unavailable</Text>
          <Text style={styles.messageBody}>
            We couldn't detect your location. Make sure location services are turned on, or search
            manually below.
          </Text>
          <PrimaryButton label="Search Manually" variant="outline" onPress={openManualSearch} style={styles.actionButton} />
          <PrimaryButton label="Try Again" variant="primary" onPress={loadPharmacies} style={styles.actionButton} />
        </View>
      </SafeAreaView>
    );
  }

  if (screenState === SCREEN_STATE.NO_RESULTS) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.centered}>
          <Ionicons name="sad-outline" size={40} color={colors.textSecondary} />
          <Text style={styles.messageTitle}>No pharmacies found nearby</Text>
          <Text style={styles.messageBody}>
            We couldn't find any pharmacies close to your location. Try searching manually instead.
          </Text>
          <PrimaryButton label="Search Manually" variant="outline" onPress={openManualSearch} style={styles.actionButton} />
        </View>
      </SafeAreaView>
    );
  }

  if (screenState === SCREEN_STATE.ERROR) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <View style={styles.centered}>
          <Ionicons name="alert-circle-outline" size={40} color={colors.textSecondary} />
          <Text style={styles.messageTitle}>Something went wrong</Text>
          <Text style={styles.messageBody}>
            We ran into a problem loading nearby pharmacies. Please check your connection and try
            again.
          </Text>
          <PrimaryButton label="Try Again" variant="primary" onPress={loadPharmacies} style={styles.actionButton} />
        </View>
      </SafeAreaView>
    );
  }

  // READY state
  return (
    <SafeAreaView style={styles.safeArea}>
      <View style={styles.header}>
        <Text style={styles.title} accessibilityRole="header">
          Nearby Pharmacies
        </Text>
        <Text style={styles.subtitle}>Tap a marker for details, then get directions.</Text>
      </View>
      <MapView
        style={styles.map}
        provider={Platform.OS === 'android' ? PROVIDER_GOOGLE : undefined}
        initialRegion={{
          latitude: userCoords.latitude,
          longitude: userCoords.longitude,
          latitudeDelta: 0.05,
          longitudeDelta: 0.05,
        }}
        showsUserLocation
        showsMyLocationButton
      >
        {pharmacies.map((pharmacy) => (
          <Marker
            key={pharmacy.id}
            coordinate={{ latitude: pharmacy.latitude, longitude: pharmacy.longitude }}
            pinColor={colors.primary}
            accessibilityLabel={`${pharmacy.name}, ${pharmacy.address}`}
          >
            <Callout onPress={() => openNavigation(pharmacy)}>
              <View style={styles.callout}>
                <Text style={styles.calloutTitle}>{pharmacy.name}</Text>
                <Text style={styles.calloutBody}>{pharmacy.address}</Text>
                {pharmacy.distanceMeters != null && (
                  <Text style={styles.calloutBody}>{formatDistance(pharmacy.distanceMeters)}</Text>
                )}
                <Text style={styles.calloutAction}>Tap to navigate &rarr;</Text>
              </View>
            </Callout>
          </Marker>
        ))}
      </MapView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.background,
  },
  header: {
    paddingHorizontal: spacing.lg,
    paddingTop: spacing.md,
    paddingBottom: spacing.sm,
  },
  title: {
    fontSize: typography.h2,
    fontWeight: '800',
    color: colors.textPrimary,
  },
  subtitle: {
    fontSize: typography.small,
    color: colors.textSecondary,
    marginTop: 2,
  },
  map: {
    flex: 1,
  },
  centered: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: spacing.xl,
  },
  messageTitle: {
    fontSize: typography.h3,
    fontWeight: '700',
    color: colors.textPrimary,
    marginTop: spacing.md,
    textAlign: 'center',
  },
  messageBody: {
    fontSize: typography.body,
    color: colors.textSecondary,
    textAlign: 'center',
    marginTop: spacing.sm,
    marginBottom: spacing.lg,
    lineHeight: 21,
  },
  actionButton: {
    width: '100%',
    marginBottom: spacing.sm,
  },
  callout: {
    minWidth: 180,
    padding: spacing.xs,
  },
  calloutTitle: {
    fontWeight: '700',
    fontSize: typography.small,
    color: colors.textPrimary,
    marginBottom: 2,
  },
  calloutBody: {
    fontSize: typography.small,
    color: colors.textSecondary,
  },
  calloutAction: {
    fontSize: typography.small,
    color: colors.primary,
    fontWeight: '700',
    marginTop: spacing.xs,
  },
});
