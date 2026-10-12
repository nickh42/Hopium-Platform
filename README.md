[README.md](https://github.com/user-attachments/files/30202752/README.md)
# Opioid Safety

A cross-platform (iOS, Android, Web) mobile app built with React Native + Expo that provides:

Emergency — a one-tap Call 988 button plus step-by-step overdose response instructions
Education — a scrollable resource center on opioids, overdose signs, naloxone use, and prevention
Nearby Pharmacies — a map that locates pharmacies (a common source of naloxone) near the user

**Disclaimer:** This app provides educational information only. It is not a substitute for professional medical advice, diagnosis, or treatment. In a life-threatening emergency, call 911.


## 1. Project Structure

```
opioid-safety-app/
├── App.js                        # Root entry point
├── app.json                      # Expo config (permissions, icons, etc.)
├── babel.config.js
├── package.json
├── .env.example                  # Template for API keys
├── src/
│   ├── screens/
│   │   ├── HomeScreen.js
│   │   ├── EmergencyScreen.js
│   │   ├── EducationScreen.js
│   │   └── PharmacyScreen.js
│   ├── components/
│   │   ├── PrimaryButton.js
│   │   ├── InfoCard.js
│   │   └── BulletList.js
│   ├── navigation/
│   │   └── BottomTabNavigator.js
│   ├── services/
│   │   ├── PhoneService.js       # Launches the dialer
│   │   ├── LocationService.js    # Requests permission + fetches GPS coords
│   │   └── PharmacyService.js    # Calls Google Places Nearby Search
│   ├── models/
│   │   └── Pharmacy.js           # Pharmacy shape + distance helper
│   └── utils/
│       ├── colors.js             # Theme (colors, spacing, typography)
│       └── constants.js          # Emergency numbers + all educational copy
```

---

## 2. Prerequisites

- [Node.js](https://nodejs.org/) 18 or later
- [Git](https://git-scm.com/)
- [Expo CLI](https://docs.expo.dev/get-started/installation/) (installed automatically via `npx`)
- A free [Expo account](https://expo.dev/signup) (only needed if you want to build install-able binaries)
- **A Google Cloud API key** with the **Maps SDK** and **Places API** enabled, for the pharmacy locator
- Xcode (Mac only, for iOS simulator) and/or Android Studio (for Android emulator) — optional if you test on a physical device with the Expo Go app instead

---

## 3. Getting an API Key (Google Maps + Places)

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (or use an existing one).
3. Enable **Maps SDK for Android**, **Maps SDK for iOS**, and **Places API**.
4. Go to **APIs & Services → Credentials → Create Credentials → API Key**.
5. (Recommended) Restrict the key to the APIs above and to your app's bundle ID / package name.

---

## 4. Local Setup

```bash
# 1. Clone your new repo (see Section 6 for how to push this project to GitHub first)
git clone https://github.com/YOUR_USERNAME/opioid-safety-app.git
cd opioid-safety-app

# 2. Install dependencies
npm install

# 3. Configure your API keys
cp .env.example .env
# then open .env and paste in your Google API key(s)

# 4. Also add your Android Maps key directly in app.json:
#    "android": { "config": { "googleMaps": { "apiKey": "YOUR_KEY" } } }

# 5. Start the Expo dev server
npx expo start
```

From the Expo dev server:
- Press `i` to open the iOS simulator (Mac only)
- Press `a` to open the Android emulator
- Or scan the QR code with the **Expo Go** app on your physical phone

---

## 5. Building Install-able Apps (optional)

To produce a real `.ipa` (iOS) or `.apk`/`.aab` (Android) file, use [EAS Build](https://docs.expo.dev/build/introduction/):

```bash
npm install -g eas-cli
eas login
eas build:configure
eas build --platform android
eas build --platform ios
```

---

## 6. Pushing This Project to GitHub

If you downloaded this project as a folder (not yet a Git repo), run the following from inside the `opioid-safety-app` folder:

```bash
# 1. Initialize git
git init

# 2. Stage and commit all files
git add .
git commit -m "Initial commit: Opioid Safety app"

# 3. Create a new empty repository on GitHub (via github.com/new),
#    then copy the remote URL it gives you and run:
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/opioid-safety-app.git
git push -u origin main
```

That's it — refresh your GitHub repository page and all the project files will be there.

**Important:** `.env` is listed in `.gitignore` so your real API keys are never committed. Only `.env.example` (with placeholder values) is pushed to GitHub.

---

## 7. Permissions Used

| Permission | Why it's needed |
| Location (foreground) | To center the map on the user and find nearby pharmacies |
| Phone / dialer | To let the Call 988 / Call 911 buttons open the device dialer |

The app never places a call automatically — it opens the dialer and the user confirms the call themselves.

---

## 8. Accessibility Notes

- All interactive elements have `accessibilityLabel` / `accessibilityRole` set.
- Bottom navigation icons are always paired with visible text labels.
- Color combinations meet WCAG AA contrast requirements.
- Touch targets are a minimum of 56px tall.
- Red is used **exclusively** for emergency actions so it always signals urgency.

---

## 9. Tech Stack

- [Expo](https://expo.dev/) (managed React Native workflow)
- [React Navigation](https://reactnavigation.org/) (bottom tabs)
- [react-native-maps](https://github.com/react-native-maps/react-native-maps)
- [expo-location](https://docs.expo.dev/versions/latest/sdk/location/)
- [expo-linking](https://docs.expo.dev/versions/latest/sdk/linking/) (dialer + external maps navigation)
- Google Places API (Nearby Search) for pharmacy data

---

## 10. License

You are free to adapt this project for your own harm-reduction / public-health use cases. If you plan to distribute it publicly, please have the medical content in `src/utils/constants.js` reviewed by a qualified healthcare professional before release.
