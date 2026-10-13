import streamlit as st

st.set_page_config(page_title="Hopium Info", page_icon="💊", layout="wide")

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(180deg, #f3fbff 0%, #edf7ff 100%);
            color: #123b5d;
            font-family: 'Times New Roman', Times, serif;
        }
        [data-testid="stSidebar"], [data-testid="stSidebarNav"], section[data-testid="stSidebar"] {
            display: none !important;
        }
        div.stButton > button {
            background: transparent !important;
            border: 1px solid transparent !important;
            box-shadow: none !important;
            color: #173d69 !important;
            font-family: 'Times New Roman', Times, serif !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            line-height: 1.1 !important;
            min-width: 180px !important;
            padding: 0.7rem 1.1rem !important;
            border-radius: 0 !important;
            margin: 0 !important;
        }
        div.stButton > button:hover {
            background: rgba(255, 255, 255, 0.2) !important;
            border: 1px solid rgba(23, 61, 105, 0.15) !important;
            border-radius: 999px !important;
        }
        .top-page-nav {
            position: fixed;
            top: 0.7rem;
            right: 1.25rem;
            left: auto;
            z-index: 1000;
            display: flex;
            justify-content: flex-end;
            align-items: center;
            gap: 1.5rem;
            padding: 0.25rem 0.2rem 0.4rem 0;
            background: rgba(243, 251, 255, 0.22);
            backdrop-filter: blur(1px);
        }
        .top-page-nav > div {
            width: max-content !important;
            margin-left: 0 !important;
        }
        .top-page-nav > div > div {
            display: flex !important;
            justify-content: flex-end !important;
            align-items: center !important;
            gap: 1.8rem !important;
        }
        .page-title {
            font-family: 'Times New Roman', Times, serif;
            font-size: 3.2rem;
            line-height: 1.1;
            margin-bottom: 0.15rem;
            text-align: center;
            animation: revealSquish 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }
        .subtitle {
            text-align: center;
            font-size: 1.08rem;
            color: #2a527b;
            margin-bottom: 1.2rem;
        }
        .reveal {
            opacity: 0;
            transform: scaleX(0.7);
            transform-origin: center;
            animation: revealSquish 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }
        @keyframes revealSquish {
            0% { opacity: 0; transform: scaleX(0.7) scaleY(0.9); filter: blur(1.4px); }
            55% { opacity: 1; transform: scaleX(0.96) scaleY(1); filter: blur(0.25px); }
            100% { opacity: 1; transform: scaleX(1) scaleY(1); filter: blur(0); }
        }
        .info-card {
            background: linear-gradient(180deg, #f7fbff 0%, #edf7ff 100%);
            border: 1px solid #d7ebff;
            border-radius: 16px;
            padding: 1rem 1.2rem;
            margin-bottom: 1rem;
            box-shadow: 0 8px 20px rgba(30, 70, 110, 0.06);
        }
        .section-tag {
            display: inline-block;
            background: #edf4ff;
            color: #214b7b;
            font-weight: 700;
            border-radius: 999px;
            padding: 0.35rem 0.8rem;
            margin-bottom: 0.8rem;
        }
        .centered-callout {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='top-page-nav'>", unsafe_allow_html=True)
info_nav, emergency_nav, narcan_nav = st.columns(3)
with info_nav:
    if st.button("Info", key="info_nav_top"):
        st.switch_page("pages/1_Info.py")
with emergency_nav:
    if st.button("Emergency", key="emergency_nav_top"):
        st.switch_page("pages/2_Emergency.py")
with narcan_nav:
    if st.button("Narcan", key="narcan_nav_top"):
        st.switch_page("pages/3_Narcan_Map.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="reveal"><h1 class="page-title">Hopium: Opioid Safety & Support</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Practical guidance for understanding opioids, spotting overdose, and getting help fast.</div>', unsafe_allow_html=True)

st.markdown('<div class="section-tag">What opioids do</div>', unsafe_allow_html=True)
col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown(
        """
        <div class="info-card">
            <h3>💊 Common effects</h3>
            <ul>
                <li>Relief from pain and pressure</li>
                <li>Sleepiness, slowed breathing, and reduced alertness</li>
                <li>Euphoria, calm, or a feeling of numbness</li>
                <li>Risk of dependence or overdose when used in high doses or mixed with other drugs</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div class="info-card">
            <h3>⚠️ Why it matters</h3>
            <ul>
                <li>Opioids can slow breathing to dangerous levels</li>
                <li>Risk rises when taken with alcohol, benzos, sleep meds, or fentanyl</li>
                <li>Even a small change in dosage can be deadly</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-tag">Signs of overdose</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="info-card">
        <h3>🚨 Look for these warning signs</h3>
        <div style="display:flex; flex-wrap:wrap; gap:12px; margin-top:0.75rem; justify-content:center;">
            <span style="background:#ffe4ef; color:#8b1e4d; border-radius:999px; padding:0.5rem 0.8rem; font-weight:600;">Blue lips or nails</span>
            <span style="background:#ffe4ef; color:#8b1e4d; border-radius:999px; padding:0.5rem 0.8rem; font-weight:600;">Very slow or stopped breathing</span>
            <span style="background:#ffe4ef; color:#8b1e4d; border-radius:999px; padding:0.5rem 0.8rem; font-weight:600;">Hard to wake up</span>
            <span style="background:#ffe4ef; color:#8b1e4d; border-radius:999px; padding:0.5rem 0.8rem; font-weight:600;">Gurgling / choking sounds</span>
            <span style="background:#ffe4ef; color:#8b1e4d; border-radius:999px; padding:0.5rem 0.8rem; font-weight:600;">Pinpoint pupils</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-tag">How to help</div>', unsafe_allow_html=True)
col3, col4 = st.columns([1, 1])
with col3:
    st.markdown(
        """
        <div class="info-card">
            <h3>🫁 Immediate response</h3>
            <ol>
                <li>Call 988 or emergency services right away.</li>
                <li>Try to wake the person and check if they’re breathing.</li>
                <li>Give naloxone if available.</li>
                <li>Start rescue breathing or CPR if needed.</li>
                <li>Place them on their side in the recovery position.</li>
            </ol>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col4:
    st.markdown(
        """
        <div class="info-card">
            <h3>🤝 What not to do</h3>
            <ul>
                <li>Do not wait to see if symptoms improve</li>
                <li>Do not leave the person alone</li>
                <li>Do not give more opioids or other sedatives</li>
                <li>Do not panic — naloxone can save a life</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<div class="section-tag">Narcan (naloxone) nasal spray</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="info-card">
        <h3>💨 How to use Narcan nasal spray</h3>
        <p>Naloxone is a medication that can reverse the effects of an opioid overdose and help restore breathing.</p>
        <ol>
            <li>Lay the person on their back.</li>
            <li>Remove the Narcan nasal spray from the box.</li>
            <li>Hold the device with your thumb on the bottom and two fingers on either side.</li>
            <li>Place the nozzle in one nostril and press firmly to spray.</li>
            <li>If there is no response in 2–3 minutes, use a second dose if available and call 988 or emergency services.</li>
        </ol>
        <p><strong>Important:</strong> Naloxone works quickly, but the person may still need emergency care because opioids can last longer than the naloxone effects.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="centered-callout"><h3>Quick safety reminder</h3></div>', unsafe_allow_html=True)
st.info(
    "If you or someone else may be overdosing, do not wait for the person to be completely unresponsive. Call 988 or local emergency services immediately and use naloxone if available."
)
