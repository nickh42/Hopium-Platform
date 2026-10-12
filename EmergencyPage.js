import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView, Alert } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import PrimaryButton from '../components/PrimaryButton';
import InfoCard from '../components/InfoCard';
import { colors, spacing, typography } from '../utils/colors';
import { callNumber } from '../services/PhoneService';
import { EMERGENCY_NUMBER, EMERGENCY_SERVICES_NUMBER, EMERGENCY_STEPS } from '../utils/constants';

export default function EmergencyScreen() {
  const handleCall988 = () => {
    Alert.alert(
      `Call ${EMERGENCY_NUMBER}?`,
      'This will open your phone dialer. If this is a life-threatening emergency, call 911 instead.',
      [
        { text: 'Cancel', style: 'cancel' },
        { text: `Call ${EMERGENCY_NUMBER}`, style: 'default', onPress: () => callNumber(EMERGENCY_NUMBER) },
      ]
    );
  };

  const handleCall911 = () => {
    callNumber(EMERGENCY_SERVICES_NUMBER);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title} accessibilityRole="header">
          Emergency
        </Text>
        <Text style={styles.subtitle}>
          If someone may be overdosing, act immediately. Every second counts.
        </Text>

        <PrimaryButton
          label={`Call ${EMERGENCY_NUMBER}`}
          variant="emergency"
          onPress={handleCall988}
          icon={<Ionicons name="call" size={24} color={colors.textOnEmergency} />}
          accessibilityHint="Opens your phone dialer to call the 988 Suicide and Crisis Lifeline"
          style={styles.mainButton}
        />

        <PrimaryButton
          label="Call 911 (Emergency Services)"
          variant="outline"
          onPress={handleCall911}
          icon={<Ionicons name="call-outline" size={22} color={colors.primary} />}
          accessibilityHint="Opens your phone dialer to call 911"
          style={styles.secondaryButton}
        />

        <InfoCard title="What to do during a suspected overdose" tone="info" icon={<Ionicons name="list" size={20} color={colors.accent} />}>
          {EMERGENCY_STEPS.map((step) => (
            <View key={step.id} style={styles.stepBlock}>
              <Text style={styles.stepTitle}>{step.title}</Text>
              <Text style={styles.stepBody}>{step.body}</Text>
            </View>
          ))}
        </InfoCard>
      </ScrollView>
    </SafeAreaView>
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
  },
  title: {
    fontSize: typography.h1,
    fontWeight: '800',
    color: colors.textPrimary,
    marginBottom: spacing.xs,
  },
  subtitle: {
    fontSize: typography.body,
    color: colors.textSecondary,
    marginBottom: spacing.lg,
  },
  mainButton: {
    marginBottom: spacing.md,
  },
  secondaryButton: {
    marginBottom: spacing.lg,
  },
  stepBlock: {
    marginBottom: spacing.md,
  },
  stepTitle: {
    fontSize: typography.body,
    fontWeight: '700',
    color: colors.textPrimary,
    marginBottom: 2,
  },
  stepBody: {
    fontSize: typography.body,
    color: colors.textSecondary,
    lineHeight: 21,
  },
});
