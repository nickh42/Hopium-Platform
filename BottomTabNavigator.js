import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Ionicons } from '@expo/vector-icons';
import HomeScreen from '../screens/HomeScreen';
import EmergencyScreen from '../screens/EmergencyScreen';
import EducationScreen from '../screens/EducationScreen';
import PharmacyScreen from '../screens/PharmacyScreen';
import { colors } from '../utils/colors';

const Tab = createBottomTabNavigator();

const ICONS = {
  Home: 'home',
  Emergency: 'alert-circle',
  Education: 'book',
  Pharmacies: 'location',
};

export default function BottomTabNavigator() {
  return (
    <Tab.Navigator
      initialRouteName="Home"
      screenOptions={({ route }) => ({
        headerShown: false,
        tabBarActiveTintColor: route.name === 'Emergency' ? colors.emergency : colors.primary,
        tabBarInactiveTintColor: colors.textSecondary,
        tabBarLabelStyle: { fontSize: 12, fontWeight: '600' },
        tabBarStyle: {
          height: 64,
          paddingBottom: 8,
          paddingTop: 6,
          borderTopColor: colors.border,
        },
        tabBarIcon: ({ color, size }) => (
          <Ionicons name={ICONS[route.name]} size={size ?? 24} color={color} />
        ),
        // Accessibility: each tab is icon + descriptive text label
        tabBarAccessibilityLabel: route.name,
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Emergency" component={EmergencyScreen} />
      <Tab.Screen name="Education" component={EducationScreen} />
      <Tab.Screen name="Pharmacies" component={PharmacyScreen} options={{ title: 'Pharmacies' }} />
    </Tab.Navigator>
  );
}
