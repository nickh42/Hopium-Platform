import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors, spacing, typography } from '../utils/colors';

/**
 * BulletList
 * Renders a list of strings as accessible bullet points.
 * Used for overdose signs, prevention tips, and naloxone steps.
 */
export default function BulletList({ items, numbered = false }) {
  return (
    <View>
      {items.map((item, index) => (
        <View
          key={index}
          style={styles.row}
          accessible
          accessibilityLabel={`${numbered ? `Step ${index + 1}: ` : ''}${item}`}
        >
          <Text style={styles.bullet}>{numbered ? `${index + 1}.` : '\u2022'}</Text>
          <Text style={styles.text}>{item}</Text>
        </View>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  row: {
    flexDirection: 'row',
    marginBottom: spacing.sm,
    alignItems: 'flex-start',
  },
  bullet: {
    fontSize: typography.body,
    fontWeight: '700',
    color: colors.primary,
    width: 28,
  },
  text: {
    fontSize: typography.body,
    color: colors.textPrimary,
    flex: 1,
    lineHeight: 22,
  },
});
