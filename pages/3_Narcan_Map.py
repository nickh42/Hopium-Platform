import urllib.parse

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Narcan Locations", page_icon="📍", layout="wide")

st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Baloo+2:wght@400;600;700;800&family=Manrope:wght@400;500;700;800&display=swap');
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(180deg, #f4fbff 0%, #edf7ff 100%);
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
        .map-note {
            background: #edf8ff;
            border: 1px solid #d8edff;
            border-radius: 12px;
            padding: 0.8rem 1rem;
            margin-bottom: 0.8rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

nav_left, info_nav, emergency_nav, narcan_nav = st.columns([6, 1, 1, 1.2])
with info_nav:
    if st.button("Info", key="info_nav_map"):
        st.switch_page("pages/1_Info.py")
with emergency_nav:
    if st.button("Emergency", key="emergency_nav_map"):
        st.switch_page("pages/2_Emergency.py")
with narcan_nav:
    if st.button("Narcan", key="narcan_nav_map"):
        st.switch_page("pages/3_Narcan_Map.py")

st.markdown('<div class="reveal"><h1 class="page-title">Find Narcan Nearby</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Search for pharmacies and nearby locations that may carry naloxone or Narcan.</div>', unsafe_allow_html=True)

search_term = st.text_input("City, ZIP code, or area", value="near me")

query = f"pharmacy naloxone Narcan {search_term}"
encoded_query = urllib.parse.quote(query)
map_url = f"https://www.google.com/maps?q={encoded_query}&output=embed"

st.markdown(
    '<div class="map-note">This page uses a Google Maps embed for nearby Narcan and pharmacy searches. Full Google Places API data would require a valid Google Cloud API key and billing enabled.</div>',
    unsafe_allow_html=True,
)

components.iframe(map_url, height=560, scrolling=True)

st.markdown('<div class="reveal"><h3 style="text-align:center;">Helpful next steps</h3></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.success("Call ahead to confirm the pharmacy has naloxone in stock.")
with col2:
    st.info("Look for emergency departments, urgent care centers, or community health clinics in your area.")
