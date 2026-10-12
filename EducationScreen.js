import React from 'react';
import { View, Text, StyleSheet, SafeAreaView, ScrollView } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import InfoCard from '../components/InfoCard';
import BulletList from '../components/BulletList';
import { colors, spacing, typography } from '../utils/colors';
import {
  OPIOID_OVERVIEW,
  HOW_OPIOIDS_AFFECT_BODY,
  OVERDOSE_SIGNS,
  NALOXONE_STEPS,
  PREVENTION_TIPS,
} from '../utils/constants';

export default function EducationScreen() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <ScrollView contentContainerStyle={styles.container}>
        <Text style={styles.title} accessibilityRole="header">
          Education
        </Text>
        <Text style={styles.subtitle}>Learn about opioids, overdose recognition, and prevention.</Text>

        <InfoCard
          title="What are opioids?"
          tone="neutral"
          icon={<Ionicons name="information-circle" size={20} color={colors.primary} />}
        >
          <Text style={styles.paragraph}>
            <Text style={styles.bold}>Prescription opioids: </Text>
            {OPIOID_OVERVIEW.prescription}
          </Text>
          <Text style={styles.paragraph}>
            <Text style={styles.bold}>Illicit opioids: </Text>
            {OPIOID_OVERVIEW.illicit}
          </Text>
          <Text style={styles.paragraph}>
            <Text style={styles.bold}>Fentanyl: </Text>
            {OPIOID_OVERVIEW.fentanyl}
          </Text>
        </InfoCard>

        <InfoCard
          title="How opioids affect the brain and body"
          tone="neutral"
          icon={<Ionicons name="pulse" size={20} color={colors.primary} />}
        >
          <Text style={styles.paragraph}>{HOW_OPIOIDS_AFFECT_BODY}</Text>
        </InfoCard>

        <InfoCard
          title="Signs of an overdose"
          tone="info"
          icon={<Ionicons name="warning" size={20} color={colors.accent} />}
        >
          <BulletList items={OVERDOSE_SIGNS} />
        </InfoCard>

        <InfoCard
          title="How to give naloxone (Narcan)"
          tone="info"
          icon={<Ionicons name="medkit" size={20} color={colors.accent} />}
        >
          <BulletList items={NALOXONE_STEPS} numbered />
        </InfoCard>

        <InfoCard
          title="Preventing an overdose"
          tone="info"
          icon={<Ionicons name="shield-checkmark" size={20} color={colors.accent} />}
        >
          <BulletList items={PREVENTION_TIPS} />
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
  paragraph: {
    fontSize: typography.body,
    color: colors.textPrimary,
    lineHeight: 22,
    marginBottom: spacing.sm,
  },
  bold: {
    fontWeight: '700',
  },
});
