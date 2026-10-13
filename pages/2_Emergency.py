import streamlit as st

st.set_page_config(page_title="Emergency", page_icon="🚨", layout="centered")

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(180deg, #f8fbff 0%, #eef7ff 100%);
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
            background: rgba(248, 251, 255, 0.22);
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
        .emergency-box {
            background: linear-gradient(180deg, #fff3f3 0%, #ffe8e8 100%);
            border: 1px solid #ffb3b3;
            border-radius: 20px;
            padding: 1.5rem;
            text-align: center;
            box-shadow: 0 14px 28px rgba(180, 31, 31, 0.08);
        }
        div.stButton > button[kind="primary"], div.stButton > button[data-testid="baseButton-secondary"], div.stButton > button[title="!"] {
            width: 290px;
            height: 290px;
            border-radius: 50%;
            background: linear-gradient(145deg, #ff3c3c, #d81d1d) !important;
            color: white !important;
            border: none !important;
            font-size: 118px !important;
            font-weight: 800 !important;
            box-shadow: 0 18px 40px rgba(200, 0, 0, 0.35);
            cursor: pointer;
            margin: 0 auto;
            display: block;
            min-width: 290px !important;
            padding: 0 !important;
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

st.markdown("<div class='top-page-nav'>", unsafe_allow_html=True)
info_nav, emergency_nav, narcan_nav = st.columns(3)
with info_nav:
    if st.button("Info", key="info_nav_emergency"):
        st.switch_page("pages/1_Info.py")
with emergency_nav:
    if st.button("Emergency", key="emergency_nav_emergency"):
        st.switch_page("pages/2_Emergency.py")
with narcan_nav:
    if st.button("Narcan", key="narcan_nav_emergency"):
        st.switch_page("pages/3_Narcan_Map.py")
st.markdown("</div>", unsafe_allow_html=True)

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
