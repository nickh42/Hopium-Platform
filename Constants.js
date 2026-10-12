/**
 * constants.js
 * App-wide constants: emergency contact numbers and static educational content.
 * Keeping educational copy here (rather than hardcoded in screens) makes it
 * easy for a clinical/content reviewer to update without touching UI code.
 */

export const EMERGENCY_NUMBER = '988'; // Suicide & Crisis Lifeline (also supports overdose-related crises in the US)
export const EMERGENCY_SERVICES_NUMBER = '911';

export const DISCLAIMER =
  'This app provides educational information only. It is not a substitute for professional medical advice, diagnosis, or treatment. If you or someone else is experiencing a medical emergency, call 911 immediately.';

export const EMERGENCY_STEPS = [
  {
    id: 'call',
    title: '1. Call for help immediately',
    body:
      'Call 911 for any suspected overdose. If you are unsure or need immediate crisis support, you can also call or text 988. Stay on the line and follow the dispatcher\u2019s instructions.',
  },
  {
    id: 'naloxone',
    title: '2. Give naloxone (Narcan) if available',
    body:
      'If you have naloxone, administer it right away. It can reverse an opioid overdose within minutes. It is safe to give even if you are not certain opioids are involved.',
  },
  {
    id: 'breathing',
    title: '3. Provide rescue breathing if trained',
    body:
      'If the person is not breathing or breathing very slowly, and you are trained, give rescue breaths: tilt the head back, pinch the nose, and give one breath every 5 seconds.',
  },
  {
    id: 'recovery',
    title: '4. Use the recovery position',
    body:
      'If the person is breathing but unresponsive, gently roll them onto their side with the top leg bent for support. This helps keep their airway clear and prevents choking.',
  },
  {
    id: 'stay',
    title: '5. Stay until help arrives',
    body:
      'Do not leave the person alone. Keep monitoring their breathing. Naloxone can wear off before the opioids do, so a second dose may be needed after 2\u20133 minutes if there is no response.',
  },
];

export const OVERDOSE_SIGNS = [
  'Slow, shallow, or stopped breathing',
  'Pinpoint (very small) pupils',
  'Bluish or grayish lips, fingernails, or skin',
  'Limp body and unresponsiveness',
  'Choking, gurgling, or snoring sounds',
  'Cold or clammy skin',
  'Unable to be woken up',
];

export const NALOXONE_STEPS = [
  'Check for signs of an opioid overdose (see above).',
  'Call 911 before or immediately after giving naloxone.',
  'Nasal spray: Peel back the packaging, tilt the person\u2019s head back, and insert the nozzle into one nostril. Press the plunger firmly to release the full dose.',
  'Injectable: Follow the specific device instructions; typically injected into the outer thigh or upper arm, even through clothing.',
  'Lay the person on their side in the recovery position after administering.',
  'Wait 2\u20133 minutes. If there is no improvement in breathing or responsiveness, give a second dose.',
  'Stay with the person until emergency responders arrive \u2014 naloxone\u2019s effects can wear off in 30\u201390 minutes, which is shorter than many opioids\u2019 effects.',
];

export const PREVENTION_TIPS = [
  'Never use opioids alone \u2014 have someone present who can respond or check in on you.',
  'Avoid mixing opioids with alcohol, benzodiazepines, or other sedatives.',
  'Carry naloxone (Narcan) and make sure people around you know how to use it.',
  'Start with a lower dose if using after a period of not using, or if trying a new supply.',
  'Learn to recognize the early warning signs of an overdose.',
  'Store prescription opioids securely and dispose of unused medication properly.',
  'Consider fentanyl test strips if using illicit substances, since fentanyl is not always detectable by smell or taste.',
];

export const OPIOID_OVERVIEW = {
  prescription:
    'Prescription opioids (such as oxycodone, hydrocodone, and morphine) are medications prescribed to manage moderate to severe pain. They can be misused or lead to dependence even when taken as prescribed.',
  illicit:
    'Illicit opioids, such as heroin, are used outside of medical supervision. Their strength and purity are unpredictable, which raises overdose risk.',
  fentanyl:
    'Fentanyl is a synthetic opioid up to 50\u2013100 times more potent than morphine. It is increasingly found mixed into other drugs, often without the user\u2019s knowledge, and is a major driver of overdose deaths.',
};

export const HOW_OPIOIDS_AFFECT_BODY =
  'Opioids attach to receptors in the brain and body that control pain and breathing. They can create feelings of pain relief and euphoria, but they also slow down the central nervous system. In high doses, this can slow or stop breathing entirely, which is what makes overdose life-threatening.';
