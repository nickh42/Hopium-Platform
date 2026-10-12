import { Linking, Alert, Platform } from 'react-native';

/**
 * PhoneService
 * Handles launching the device dialer for emergency calls.
 */

/**
 * Opens the device's phone dialer with the given number pre-filled.
 * On most platforms `tel:` URLs open the dialer with the number ready to call;
 * the user still confirms the call themselves. This is intentional so the app
 * never places a call without explicit user action, which is both an
 * accessibility/permissions requirement and a safety-conscious default.
 */
export async function callNumber(number) {
  const url = Platform.select({
    ios: `telprompt:${number}`,
    android: `tel:${number}`,
    default: `tel:${number}`,
  });

  try {
    const supported = await Linking.canOpenURL(url);
    if (supported) {
      await Linking.openURL(url);
    } else {
      Alert.alert(
        'Unable to place call',
        `Your device could not open the dialer. Please manually call ${number}.`
      );
    }
  } catch (error) {
    Alert.alert(
      'Something went wrong',
      `We couldn't start the call automatically. Please manually dial ${number}.`
    );
  }
}

export default { callNumber };
