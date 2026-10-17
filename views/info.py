import streamlit as st

from hopium.graphics import ICONS, NARCAN_DEVICE
from hopium.ui import cards

st.title("Opioid Information")
st.caption(
    "General education based on CDC and SAMHSA guidance and the Narcan (naloxone) "
    "manufacturer instructions. It is not a substitute for medical advice."
)

st.header("Effects of opioids")
st.write(
    "Opioids include prescription pain medicines (oxycodone, hydrocodone, morphine), "
    "heroin, and fentanyl. They attach to receptors in the brain and body that control pain and breathing."
)
cards([
    (ICONS["pain"], "Pain relief & euphoria", "A feeling of calm or well-being that can make use hard to stop."),
    (ICONS["drowsy"], "Drowsiness & confusion", "Heavy sleepiness, slowed thinking, poor coordination."),
    (ICONS["nausea"], "Nausea & constipation", "Common even at prescribed doses."),
    (ICONS["breathing"], "Slowed breathing", "The most dangerous effect. High doses can stop breathing."),
    (ICONS["dependence"], "Tolerance & dependence", "Regular use needs higher doses and can lead to opioid use disorder."),
])
st.markdown(
    '<div class="hp-callout"><b>Fentanyl warning:</b> Fentanyl is far stronger than other opioids and is '
    "found in counterfeit pills and other drugs. Someone may take it without knowing.</div>",
    unsafe_allow_html=True,
)

st.header("How to spot signs of an overdose")
cards([
    (ICONS["pupils"], "Tiny pupils", "Pinpoint pupils, even in a dim room."),
    (ICONS["unresponsive"], "Can't be woken", "Unconscious, limp, or does not respond to voice or touch."),
    (ICONS["slow_breath"], "Slow or no breathing", "Breathing is very slow, shallow, or has stopped."),
    (ICONS["gurgle"], "Gurgling sounds", "Choking, snoring, or gurgling noises."),
    (ICONS["blue_lips"], "Blue or purple lips", "Lips and fingernails turn blue, purple, or gray."),
    (ICONS["cold"], "Pale, clammy skin", "Cold, sweaty, pale skin."),
])

st.header("How to help someone who is overdosing")
cards([
    (ICONS["wake"], "Try to wake them", "Shout their name and rub your knuckles hard on the middle of their chest."),
    (ICONS["call"], "Call 911", "Tell the dispatcher the person is not breathing. Stay on the line."),
    (ICONS["spray"], "Give Narcan", "Use naloxone nasal spray right away (steps below)."),
    (ICONS["side"], "Recovery position", "If they are breathing but unresponsive, turn them on their side. "
                                           "If not breathing, give rescue breaths or CPR if you know how."),
    (ICONS["stay"], "Stay with them", "If there is no response after 2 to 3 minutes, give another dose. "
                                       "Naloxone can wear off, so stay until help arrives."),
], step=True)
st.markdown(
    '<div class="hp-callout">Many states have Good Samaritan laws that protect people who call for help during an overdose.</div>',
    unsafe_allow_html=True,
)

st.header("Narcan nasal spray")
st.write(
    "Narcan (naloxone) quickly reverses an opioid overdose by blocking opioids in the brain. "
    "It only works on opioids, is safe if the person turns out not to have taken any, and cannot be used to get high. "
    "It comes ready to use: no assembly, priming, or testing."
)
st.markdown(f'<div class="hp-device">{NARCAN_DEVICE}</div>', unsafe_allow_html=True)
cards([
    (ICONS["n_peel"], "Peel back the package", "Remove the device from the box and peel back the tab. Do not press the plunger yet."),
    (ICONS["n_hold"], "Hold it correctly", "Thumb on the bottom of the plunger. First and middle fingers on either side of the nozzle."),
    (ICONS["n_insert"], "Tilt head back, insert", "Lay the person on their back, tilt the head back, and put the nozzle in one nostril until your fingers touch the nose."),
    (ICONS["n_press"], "Press firmly", "Push the plunger all the way to give the dose, then remove the device."),
    (ICONS["n_repeat"], "Turn on side, repeat if needed", "Roll them on their side. After 2 to 3 minutes with no response, give a new device in the other nostril."),
], step=True)
st.caption("Sources: CDC Overdose Prevention, SAMHSA Naloxone resources, and the Narcan Nasal Spray instructions for use.")
