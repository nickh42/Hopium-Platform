import streamlit as st

st.set_page_config(page_title="Emergency", page_icon="🚨", layout="centered")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Manrope:wght@400;500;700;800&display=swap');
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(180deg, #f8fbff 0%, #eef7ff 100%);
            color: #123b5d;
            font-family: 'Manrope', sans-serif;
        }
        [data-testid="stSidebarNav"] { display: none; }
        .top-nav button {
            border-radius: 999px;
            border: 1px solid rgba(34, 91, 151, 0.18);
            background: rgba(255,255,255,0.72);
            color: #173d69;
            font-weight: 700;
            padding: 0.5rem 1rem;
            min-width: 90px;
        }
        .page-title {
            font-family: 'Baloo 2', cursive;
            font-size: 3rem;
            line-height: 1.1;
            margin-bottom: 0.15rem;
            text-align: center;
        }
        .subtitle {
            text-align: center;
            font-size: 1.02rem;
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
        .emergency-box {
            background: linear-gradient(180deg, #fff3f3 0%, #ffe8e8 100%);
            border: 1px solid #ffb3b3;
            border-radius: 20px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 14px 28px rgba(180, 31, 31, 0.08);
        }
        div.stButton > button {
            width: 260px;
            height: 260px;
            border-radius: 50%;
            background: linear-gradient(145deg, #ff3c3c, #d81d1d);
            color: white;
            border: none;
            font-size: 110px;
            font-weight: 800;
            box-shadow: 0 18px 40px rgba(200, 0, 0, 0.35);
            cursor: pointer;
            margin: 0 auto;
            display: block;
        }
        div.stButton > button:hover {
            transform: scale(1.02);
            box-shadow: 0 24px 50px rgba(200, 0, 0, 0.42);
        }
        .centered-note {
            text-align: center;
            margin-top: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

nav_left, info_nav, emergency_nav, narcan_nav = st.columns([6, 1, 1, 1.2])
with info_nav:
    if st.button("Info", key="info_nav_emergency"):
        st.switch_page("pages/1_Info.py")
with emergency_nav:
    if st.button("Emergency", key="emergency_nav_emergency"):
        st.switch_page("pages/2_Emergency.py")
with narcan_nav:
    if st.button("Narcan", key="narcan_nav_emergency"):
        st.switch_page("pages/3_Narcan_Map.py")

st.markdown('<div class="reveal"><h1 class="page-title">Emergency Help</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Immediate support for someone who may be overdosing.</div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="emergency-box">
        <h3>Immediate support</h3>
        <p>If someone is unresponsive or not breathing, call 988 or emergency services right away.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

@st.dialog("Are you sure you want to call 988?")
def confirm_call_988():
    st.warning("988 is for crisis support and emotional support. If the person is not breathing or has no pulse, call emergency services immediately.")
    col_a, col_b = st.columns(2)
    with col_a:
        if st.button("Yes, open 988", use_container_width=True):
            st.components.v1.html("<script>window.open('https://988lifeline.org/', '_blank');</script>", height=0)
            st.success("Opening the 988 Lifeline website in a new tab.")
    with col_b:
        if st.button("No, stay here", use_container_width=True):
            st.rerun()

if st.button("!", key="large_emergency_button", help="Call 988"):
    confirm_call_988()

st.markdown('<div class="centered-note">Tap the red button above to confirm before opening the 988 Lifeline support page.</div>', unsafe_allow_html=True)
