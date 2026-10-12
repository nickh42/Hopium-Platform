import React from 'react';
import { Pressable, Text, StyleSheet, View } from 'react-native';
import { colors, spacing, typography, radius } from '../utils/colors';

/**
 * PrimaryButton
 * A large, accessible, rounded button used across the app.
 *
 * variant: 'primary' | 'emergency' | 'outline'
 *   - 'primary'   : standard blue action button
 *   - 'emergency' : red button, reserved for emergency actions only
 *   - 'outline'   : secondary/tertiary action
 */
export default function PrimaryButton({
  label,
  onPress,
  icon = null,
  variant = 'primary',
  accessibilityHint,
  style,
}) {
  const variantStyles = {
    primary: {
      backgroundColor: colors.primary,
      textColor: colors.textOnPrimary,
      borderColor: colors.primary,
    },
    emergency: {
      backgroundColor: colors.emergency,
      textColor: colors.textOnEmergency,
      borderColor: colors.emergency,
    },
    outline: {
      backgroundColor: colors.background,
      textColor: colors.primary,
      borderColor: colors.primary,
    },
  };

  const current = variantStyles[variant] || variantStyles.primary;

  return (
    <Pressable
      onPress={onPress}
      accessibilityRole="button"
      accessibilityLabel={label}
      accessibilityHint={accessibilityHint}
      hitSlop={8}
      style={({ pressed }) => [
        styles.button,
        {
          backgroundColor: current.backgroundColor,
          borderColor: current.borderColor,
          opacity: pressed ? 0.85 : 1,
        },
        style,
      ]}
    >
      <View style={styles.content}>
        {icon && <View style={styles.icon}>{icon}</View>}
        <Text style={[styles.label, { color: current.textColor }]}>{label}</Text>
      </View>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  button: {
    minHeight: 56,
    borderRadius: radius.lg,
    borderWidth: 2,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    justifyContent: 'center',
    alignItems: 'center',
    // Generous touch target and spacing per accessibility requirements
  },
  content: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
  },
  icon: {
    marginRight: spacing.sm,
  },
  label: {
    fontSize: typography.button,
    fontWeight: '700',
    textAlign: 'center',
  },
});
