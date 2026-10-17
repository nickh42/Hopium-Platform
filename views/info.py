import streamlit as st

from hopium.graphics import ICONS
from hopium.ui import callout, cards, large_layout

large_layout()

st.title("Opioid Information")
st.caption(
    "General education based on CDC, SAMHSA and FDA guidance and the Narcan (naloxone) "
    "manufacturer instructions. It is not a substitute for medical advice."
)

# ---------------------------------------------------------------- Effects
st.header("Effects of opioids")
st.write(
    "Opioids are drugs that attach to opioid receptors in the brain, spinal cord and gut. "
    "Those receptors control pain, mood, and, importantly, breathing. They include:"
)
st.markdown(
    "- **Prescription pain medicines:** oxycodone, hydrocodone, morphine, codeine, methadone, tramadol\n"
    "- **Illicit opioids:** heroin and illegally made fentanyl\n"
    "- **Medicines used to treat opioid use disorder:** buprenorphine and methadone (taken as directed, "
    "these are treatment, not misuse)"
)

st.subheader("Short-term effects")
cards([
    (ICONS["pain"], "Pain relief & euphoria", "Pain fades and many people feel warm, calm or relaxed. That reward is what makes use hard to stop."),
    (ICONS["drowsy"], "Drowsiness & confusion", "Heavy sleepiness, slowed thinking, slurred speech and poor coordination. Falls and accidents are more likely."),
    (ICONS["nausea"], "Nausea & constipation", "Very common, even at prescribed doses. Itching, dry mouth and flushed skin can also occur."),
    (ICONS["breathing"], "Slowed breathing", "The most dangerous effect. Breathing becomes slow and shallow, lowering oxygen to the brain and heart."),
])

st.subheader("Long-term effects")
cards([
    (ICONS["dependence"], "Tolerance", "The body adapts, so the same dose does less. People take more, which raises overdose risk."),
    (ICONS["dependence"], "Physical dependence", "Stopping suddenly causes withdrawal: aches, sweating, anxiety, vomiting, diarrhea and insomnia."),
    (ICONS["pain"], "Opioid use disorder", "Continued use despite harm, cravings, and loss of control. It is a treatable medical condition."),
    (ICONS["drowsy"], "Other health effects", "Low hormone levels, sleep problems, depression, and heightened pain sensitivity over time."),
])

st.subheader("What raises the risk of overdose")
st.markdown(
    "- **Fentanyl.** It is about 50 times stronger than heroin and is often mixed into counterfeit pills and other drugs, "
    "so people can take it without knowing. A tiny amount can be fatal.\n"
    "- **Mixing with other sedatives.** Alcohol, benzodiazepines (such as Xanax or Valium), sleep medicines and "
    "xylazine all deepen sedation and further slow breathing.\n"
    "- **Lost tolerance.** After detox, jail, hospital stays or treatment, tolerance drops fast. Returning to a previous dose "
    "is a leading cause of fatal overdose.\n"
    "- **Using alone.** If something goes wrong, no one is there to call for help or give naloxone.\n"
    "- **Higher doses, injecting, or taking pills not prescribed to you.**\n"
    "- **Health conditions** such as lung, heart or liver disease, or sleep apnea."
)
callout(
    "<b>Pills from friends, social media or the street can contain fentanyl.</b> Only pills from a pharmacy "
    "are reliably what the label says."
)

# ---------------------------------------------------------------- Signs
st.header("How to spot signs of an overdose")
st.write(
    "An overdose can look like heavy sleep, so the key question is: can the person be woken, and are they breathing normally? "
    "Look for these signs, especially several together:"
)
cards([
    (ICONS["pupils"], "Tiny pupils", "Pupils shrink to pinpoints, even in dim light."),
    (ICONS["unresponsive"], "Can't be woken", "Limp body. No response to shouting, shaking, or a firm rub on the chest."),
    (ICONS["slow_breath"], "Slow or no breathing", "Fewer than about 8 breaths a minute, shallow, uneven, or stopped."),
    (ICONS["gurgle"], "Gurgling sounds", "Choking, deep snoring or a gurgling noise (sometimes called the death rattle)."),
    (ICONS["blue_lips"], "Blue or purple lips", "Lips and fingertips turn blue, purple or gray. On darker skin it may look ashen or gray."),
    (ICONS["cold"], "Pale, clammy skin", "Cold, sweaty skin with a weak or slow pulse."),
])
st.subheader("Overdose or just very high?")
st.markdown(
    "| | **Very high / sedated** | **Overdose** |\n"
    "|---|---|---|\n"
    "| Waking up | Wakes when shouted at or shaken | Cannot be woken |\n"
    "| Breathing | Slow but steady, normal snoring | Very slow, gurgling, irregular, or stopped |\n"
    "| Skin color | Normal | Blue, purple, gray or very pale |\n"
    "| Body | Drowsy but holds posture | Limp |\n"
)
callout("<b>If you're not sure, treat it as an overdose.</b> Naloxone is safe to give even if opioids are not involved.")

# ---------------------------------------------------------------- Helping
st.header("How to help someone who is overdosing")
cards([
    (ICONS["wake"], "Check responsiveness", "Shout their name. Rub your knuckles hard up and down the middle of their breastbone for 5 to 10 seconds."),
    (ICONS["call"], "Call 911", "Say \"someone is unresponsive and not breathing.\" Give your location. Put the phone on speaker and follow instructions."),
    (ICONS["spray"], "Give naloxone", "Use Narcan nasal spray right away. Steps are in the next section."),
    (ICONS["slow_breath"], "Support breathing", "If they are not breathing, tilt the head back, pinch the nose and give 1 breath every 5 seconds. If trained, do CPR."),
    (ICONS["side"], "Recovery position", "Once breathing, roll them onto their side with the top knee bent so they can't choke if they vomit."),
    (ICONS["stay"], "Stay and watch", "If there's no response after 2 to 3 minutes, give another dose. Stay until help arrives."),
], step=True)

st.subheader("Do and don't")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        "**Do**\n\n"
        "- Act fast: brain damage can begin within minutes without oxygen\n"
        "- Give a second dose if there's no response\n"
        "- Tell responders what was taken, if you know\n"
        "- Stay with the person for at least 2 hours, even if they wake up"
    )
with col2:
    st.markdown(
        "**Don't**\n\n"
        "- Don't leave them alone to \"sleep it off\"\n"
        "- Don't put them in a cold shower, or give ice, coffee or food\n"
        "- Don't induce vomiting\n"
        "- Don't inject them with anything else, including stimulants"
    )
callout(
    "<b>Legal protection:</b> Most U.S. states have Good Samaritan laws that protect people who call for help "
    "during an overdose from certain drug possession charges. Laws vary by state."
)

callout(
    "<b>Have naloxone?</b> See the full <b>Narcan Guide</b> page (top right) for step-by-step instructions, "
    "what to expect afterward, and storage tips."
)

# ---------------------------------------------------------------- Prevention
st.header("Preventing overdose and getting help")
st.markdown(
    "- **Never use alone**, or ask someone to check on you.\n"
    "- **Start with a small amount** if you've taken a break, and don't mix substances.\n"
    "- **Fentanyl test strips** can detect fentanyl in drugs, but they aren't perfect. Where legal, they're a useful extra step.\n"
    "- **Treatment works.** Medicines like buprenorphine, methadone and naltrexone reduce cravings and overdose risk and are "
    "the gold standard for opioid use disorder.\n"
    "- **SAMHSA National Helpline:** 1-800-662-4357 (free, confidential, 24/7, English and Spanish).\n"
    "- **Find treatment:** findtreatment.gov"
)
st.caption(
    "Sources: CDC Overdose Prevention, SAMHSA Opioid Overdose Prevention Toolkit, FDA naloxone guidance, "
    "and the Narcan Nasal Spray instructions for use."
)
