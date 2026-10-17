import streamlit as st

from hopium.graphics import ICONS, NARCAN_DEVICE
from hopium.ui import callout, cards

st.title("Narcan Nasal Spray Guide")
st.caption("Based on the Narcan Nasal Spray instructions for use and CDC and SAMHSA guidance. Not a substitute for medical advice.")
callout("<b>Opioid overdose is an emergency.</b> Give Narcan, call 911, and stay with the person.")

st.write(
    "Narcan is a brand of naloxone, a medicine that quickly reverses an opioid overdose by knocking opioids off the receptors "
    "in the brain so breathing can restart. The nasal spray comes ready to use: **no assembly, no priming, no testing.**"
)
st.markdown(f'<div class="hp-device">{NARCAN_DEVICE}</div>', unsafe_allow_html=True)

st.subheader("Step by step")
cards([
    (ICONS["n_peel"], "Open the package", "Peel back the tab and remove the device. Don't press the plunger yet: each device holds exactly one dose."),
    (ICONS["n_hold"], "Hold it correctly", "Thumb on the bottom of the plunger. First and middle fingers on either side of the nozzle."),
    (ICONS["n_insert"], "Position the person", "Lay them on their back and tilt the head back. Support the neck with your hand."),
    (ICONS["n_insert"], "Insert the nozzle", "Gently put the tip in one nostril until your fingers touch the bottom of the nose."),
    (ICONS["n_press"], "Press firmly", "Push the plunger all the way in to release the dose. Then take the device out."),
    (ICONS["side"], "Turn them on their side", "Recovery position. Call 911 if you haven't already."),
    (ICONS["n_repeat"], "Repeat if needed", "If no response in 2 to 3 minutes, use a new device in the other nostril. Keep going every 2 to 3 minutes."),
], step=True)

st.subheader("What to expect after Narcan")
st.markdown(
    "- It starts working in about 2 to 5 minutes. The person may wake suddenly, confused, or in withdrawal.\n"
    "- **Withdrawal symptoms** can include body aches, sweating, shaking, nausea, vomiting, diarrhea, a fast heartbeat "
    "and agitation. They're uncomfortable but not usually life-threatening. Try to keep the person calm and discourage "
    "them from using more opioids to \"fix\" it.\n"
    "- **Narcan wears off in 30 to 90 minutes**, but some opioids (especially fentanyl and methadone) last longer. "
    "The overdose can return, so the person must get medical care even if they seem fine."
)

st.subheader("Good to know")
st.markdown(
    "- **Safe for everyone:** adults, children, pregnant people and older adults. It has no effect if opioids aren't present, "
    "and it cannot be misused to get high.\n"
    "- **It only works on opioids.** It does not reverse alcohol, benzodiazepines or stimulant overdoses, but it is still safe "
    "to try when you're unsure.\n"
    "- **Available without a prescription** at U.S. pharmacies since 2023. Many health departments and community programs give it away free.\n"
    "- **Storage:** keep at room temperature, away from heat and direct light, and don't freeze it. "
    "Check the expiration date printed on the package and replace expired devices. Keep two doses together.\n"
    "- **Injectable naloxone** and other nasal products exist too. The idea is the same: give it, call 911, repeat if needed.\n"
    "- **Carry it:** if you or someone you know uses opioids, or takes prescription opioids, keep naloxone where people can find it."
)
