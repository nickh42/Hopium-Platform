/**
 * colors.js
 * Centralized color palette for the Opioid Safety app.
 *
 * Design intent:
 * - White backgrounds for a clean, calming, clinical feel.
 * - Blue as the primary brand / navigation color.
 * - Green reserved for informational / educational / "safe" elements.
 * - Red reserved EXCLUSIVELY for emergency actions, so it always signals urgency.
 * - All foreground/background pairs meet WCAG AA contrast ratios (4.5:1+).
 */

export const colors = {
  // Core backgrounds
  background: '#FFFFFF',
  surface: '#F5F8FC',
  border: '#E1E8F0',

  // Brand / primary
  primary: '#1565C0', // blue
  primaryDark: '#0D47A1',
  primaryLight: '#E3F2FD',

  // Informational / educational accents
  accent: '#2E7D32', // green
  accentLight: '#E8F5E9',

  // Emergency — reserved ONLY for emergency call-to-action and critical alerts
  emergency: '#C62828', // red
  emergencyDark: '#8E0000',
  emergencyLight: '#FFEBEE',

  // Text
  textPrimary: '#1A1A1A',
  textSecondary: '#4A4A4A',
  textOnPrimary: '#FFFFFF',
  textOnEmergency: '#FFFFFF',

  // Utility
  disabled: '#B0BEC5',
  shadow: '#000000',
  white: '#FFFFFF',
  black: '#000000',
};

export const spacing = {
  xs: 4,
  sm: 8,
  md: 16,
  lg: 24,
  xl: 32,
  xxl: 48,
};

export const typography = {
  h1: 28,
  h2: 22,
  h3: 18,
  body: 16,
  small: 14,
  button: 18,
};

export const radius = {
  sm: 8,
  md: 12,
  lg: 20,
  pill: 999,
};

export default colors;
