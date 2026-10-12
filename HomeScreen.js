import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { colors, spacing, typography, radius } from '../utils/colors';
import { DISCLAIMER } from '../utils/constants';

export default function HomeScreen() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <View style={styles.iconWrap} accessibilityElementsHidden importantForAccessibility="no">
          <Ionicons name="medkit" size={56} color={colors.primary} />
        </View>

        <Text style={styles.title} accessibilityRole="header">
          Opioid Safety
        </Text>

        <Text style={styles.description}>
          Fast access to overdose emergency support, clear education on opioids and naloxone, and
          a locator to find nearby pharmacies.
        </Text>

        <View style={styles.featureRow}>
          <FeaturePill icon="alert-circle" label="Emergency" color={colors.emergency} />
          <FeaturePill icon="book" label="Education" color={colors.accent} />
          <FeaturePill icon="location" label="Pharmacies" color={colors.primary} />
        </View>

        <View style={styles.disclaimerBox} accessible accessibilityRole="alert">
          <Ionicons
            name="information-circle-outline"
            size={22}
            color={colors.textSecondary}
            style={{ marginRight: spacing.sm }}
          />
          <Text style={styles.disclaimerText}>{DISCLAIMER}</Text>
        </View>

        <Text style={styles.hint}>Use the tabs below to get started.</Text>
      </ScrollView>
    </SafeAreaView>
  );
}

function FeaturePill({ icon, label, color }) {
  return (
    <View style={styles.pill} accessible accessibilityLabel={label}>
      <Ionicons name={icon} size={22} color={color} />
      <Text style={[styles.pillLabel, { color }]}>{label}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: colors.background,
  },
  container: {
    padding: spacing.lg,
    paddingBottom: spacing.xxl,
    alignItems: 'center',
  },
  iconWrap: {
    marginTop: spacing.lg,
    marginBottom: spacing.sm,
  },
  title: {
    fontSize: typography.h1,
    fontWeight: '800',
    color: colors.textPrimary,
    marginBottom: spacing.sm,
    textAlign: 'center',
  },
  description: {
    fontSize: typography.body,
    color: colors.textSecondary,
    textAlign: 'center',
    lineHeight: 22,
    marginBottom: spacing.lg,
  },
  featureRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: spacing.lg,
  },
  pill: {
    flex: 1,
    alignItems: 'center',
    backgroundColor: colors.surface,
    borderRadius: radius.md,
    paddingVertical: spacing.md,
    marginHorizontal: spacing.xs,
  },
  pillLabel: {
    marginTop: spacing.xs,
    fontSize: typography.small,
    fontWeight: '700',
  },
  disclaimerBox: {
    flexDirection: 'row',
    backgroundColor: colors.surface,
    borderRadius: radius.md,
    padding: spacing.md,
    marginTop: spacing.md,
  },
  disclaimerText: {
    flex: 1,
    fontSize: typography.small,
    color: colors.textSecondary,
    lineHeight: 20,
  },
  hint: {
    marginTop: spacing.lg,
    fontSize: typography.small,
    color: colors.textSecondary,
  },
});
