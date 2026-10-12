import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors, spacing, typography, radius } from '../utils/colors';

/**
 * InfoCard
 * A card container used to group related educational or informational content.
 * `tone` controls the accent color: 'info' (green, default) or 'neutral' (blue-gray).
 */
export default function InfoCard({ title, children, tone = 'info', icon = null }) {
  const accentColor = tone === 'info' ? colors.accent : colors.primary;
  const backgroundColor = tone === 'info' ? colors.accentLight : colors.primaryLight;

  return (
    <View
      style={[styles.card, { borderLeftColor: accentColor, backgroundColor }]}
      accessible
      accessibilityRole="summary"
    >
      <View style={styles.headerRow}>
        {icon && <View style={styles.icon}>{icon}</View>}
        <Text style={[styles.title, { color: colors.textPrimary }]} accessibilityRole="header">
          {title}
        </Text>
      </View>
      <View style={styles.body}>{children}</View>
    </View>
  );
}

const styles = StyleSheet.create({
  card: {
    borderRadius: radius.md,
    borderLeftWidth: 5,
    padding: spacing.md,
    marginBottom: spacing.md,
  },
  headerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  icon: {
    marginRight: spacing.sm,
  },
  title: {
    fontSize: typography.h3,
    fontWeight: '700',
    flexShrink: 1,
  },
  body: {
    marginTop: spacing.xs,
  },
});
