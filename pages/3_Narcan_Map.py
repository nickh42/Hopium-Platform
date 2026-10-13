import urllib.parse

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Narcan Locations", page_icon="📍", layout="wide")

st.markdown(
    """
    <style>
        html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
            background: linear-gradient(180deg, #f4fbff 0%, #edf7ff 100%);
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
            background: rgba(244, 251, 255, 0.22);
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

st.markdown("<div class='top-page-nav'>", unsafe_allow_html=True)
info_nav, emergency_nav, narcan_nav = st.columns(3)
with info_nav:
    if st.button("Info", key="info_nav_map"):
        st.switch_page("pages/1_Info.py")
with emergency_nav:
    if st.button("Emergency", key="emergency_nav_map"):
        st.switch_page("pages/2_Emergency.py")
with narcan_nav:
    if st.button("Narcan", key="narcan_nav_map"):
        st.switch_page("pages/3_Narcan_Map.py")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown('<div class="reveal"><h1 class="page-title">Find Narcan Nearby</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Search for pharmacies and nearby locations that may carry naloxone or Narcan.</div>', unsafe_allow_html=True)

if "search_term" not in st.session_state:
    st.session_state.search_term = "pharmacies near me"

col_search, col_loc = st.columns([4, 1.6])
with col_search:
    st.session_state.search_term = st.text_input("City, ZIP code, or area", value=st.session_state.search_term)
with col_loc:
    st.markdown(
        """
        <button id="use-my-location-btn" style="width: 100%; background: #173d69; color: white; border: none; border-radius: 999px; padding: 0.75rem 1rem; font-size: 1rem; font-weight: 700; cursor: pointer; font-family: 'Times New Roman', Times, serif;">
            Use my location
        </button>
        """,
        unsafe_allow_html=True,
    )

search_term = (st.session_state.search_term or "").strip() or "pharmacies near me"
query = "pharmacies near me" if search_term.lower() == "pharmacies near me" else f"pharmacy naloxone Narcan {search_term}"
encoded_query = urllib.parse.quote(query)
base_map_url = f"https://www.google.com/maps?q={encoded_query}&output=embed"

st.markdown(
    '<div class="map-note">This page uses a Google Maps embed for nearby Narcan and pharmacy searches. The “Use my location” button requests your device location and centers the map on nearby pharmacies.</div>',
    unsafe_allow_html=True,
)

map_html = f"""
<div id="location-message" style="display:none; margin-bottom: 0.75rem; padding: 0.75rem 1rem; border-radius: 12px; background: #fff3f3; border: 1px solid #f3c5c5; color: #7a2a2a; font-weight: 600;">
    Location access was denied. Please enter a city or ZIP code instead.
</div>
<div id="map-shell" style="width:100%; min-height:560px;">
    <iframe id="narcan-map-frame" src="{base_map_url}" width="100%" height="560" style="border:0; border-radius: 14px;" loading="lazy" allowfullscreen referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
<script>
    const mapFrame = document.getElementById('narcan-map-frame');
    const button = document.getElementById('use-my-location-btn');
    const messageBox = document.getElementById('location-message');
    if (button) {{
        button.addEventListener('click', function() {{
            if (!navigator.geolocation) {{
                messageBox.textContent = 'Location access is not supported in this browser. Please enter a city or ZIP code instead.';
                messageBox.style.display = 'block';
                return;
            }}

            navigator.geolocation.getCurrentPosition(function(position) {{
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;
                const centerMapUrl = 'https://www.google.com/maps?q=pharmacies+near+me&center=' + lat + ',' + lng + '&z=13&output=embed';
                mapFrame.src = centerMapUrl;
                mapFrame.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
                messageBox.style.display = 'none';
            }}, function(error) {{
                let msg = 'Location access was denied. Please enter a city or ZIP code instead.';
                if (error && error.code === 2) {{
                    msg = 'Location is unavailable right now. Please enter a city or ZIP code instead.';
                }} else if (error && error.code === 3) {{
                    msg = 'Location request timed out. Please enter a city or ZIP code instead.';
                }}
                messageBox.textContent = msg;
                messageBox.style.display = 'block';
            }}, {{ enableHighAccuracy: true, timeout: 15000, maximumAge: 0 }});
        }});
    }}
</script>
"""
st.markdown(map_html, unsafe_allow_html=True)

st.markdown('<div class="reveal"><h3 style="text-align:center;">Helpful next steps</h3></div>', unsafe_allow_html=True)
col1, col2 = st.columns(2)
with col1:
    st.success("Call ahead to confirm the pharmacy has naloxone in stock.")
with col2:
    st.info("Look for emergency departments, urgent care centers, or community health clinics in your area.")
