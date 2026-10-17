import streamlit as st

from hopium.ui import header, inject_css, splash_once

st.set_page_config(page_title="Hopium", page_icon="💗", layout="centered", initial_sidebar_state="collapsed")
inject_css()
splash_once()
header()

pages = [
    st.Page("views/info.py", title="Info", icon="📘", default=True),
    st.Page("views/narcan.py", title="Narcan Guide", icon="💊"),
    st.Page("views/help_988.py", title="988 Help", icon="🆘"),
    st.Page("views/map.py", title="Find Narcan", icon="📍"),
]
st.navigation(pages, position="top").run()
