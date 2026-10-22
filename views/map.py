import os

import pydeck as pdk
import streamlit as st

from hopium.places import PlacesError, apple_directions_url, directions_url, geocode, nearby_pharmacies
from hopium.ui import callout

st.title("Find Narcan near you")


def api_key() -> str:
    try:
        return st.secrets["GOOGLE_MAPS_API_KEY"]
    except Exception:
        return os.environ.get("GOOGLE_MAPS_API_KEY", "")


key = api_key()
if not key:
    st.info(
        "The map needs a Google API key. Add `GOOGLE_MAPS_API_KEY` to `.streamlit/secrets.toml` "
        "(see `.streamlit/secrets.toml.example`) or to your app's Secrets settings, then restart. "
        "Enable **Geocoding API** and **Places API (New)** for the key."
    )
    st.stop()


@st.cache_data(ttl=3600, show_spinner=False)
def search(address: str, radius_km: int):
    found = geocode(address, key)
    if not found:
        return None
    lat, lng, label = found
    return lat, lng, label, nearby_pharmacies(lat, lng, key, radius_km * 1000)


callout(
    "Most U.S. pharmacies can dispense naloxone, but stock varies. Google does not show whether Narcan "
    "is on the shelf, so <b>call ahead to confirm</b>."
)

with st.form("find"):
    address = st.text_input("Your address, city, or ZIP code", placeholder="e.g. 02139 or 100 Main St, Springfield")
    radius_km = st.select_slider("Search distance", options=[2, 5, 8, 15, 25], value=8, format_func=lambda k: f"{k} km")
    go = st.form_submit_button("Search")

if go and not address.strip():
    st.warning("Enter an address or ZIP code first.")
elif go:
    try:
        with st.spinner("Looking for pharmacies..."):
            result = search(address.strip(), radius_km)
    except PlacesError as e:
        st.error(str(e))
        st.stop()
    if result is None:
        st.warning("Google couldn't find that location. Try a fuller address or a ZIP code.")
    else:
        lat, lng, label, places = result
        st.subheader(f"Pharmacies near {label}")
        if not places:
            st.info("No pharmacies found in that area. Try a wider search distance.")
        else:
            data = [{"lat": lat, "lon": lng, "name": "You are here", "color": [31, 59, 87]}] + [
                {"lat": p["lat"], "lon": p["lon"], "name": p["name"], "color": [194, 65, 127]} for p in places
            ]
            st.pydeck_chart(
                pdk.Deck(
                    layers=[pdk.Layer("ScatterplotLayer", data, get_position="[lon, lat]", get_fill_color="color",
                                      get_radius=90, radius_min_pixels=7, pickable=True)],
                    initial_view_state=pdk.ViewState(latitude=lat, longitude=lng, zoom=11.5),
                    tooltip={"text": "{name}"},
                ),
                use_container_width=True,
            )
            for p in places:
                phone = f" · {p['phone']}" if p["phone"] else ""
                st.markdown(
                    f"**{p['name']}**  \n{p['address']}{phone}  \n"
                    f"[Get directions]({directions_url(lat, lng, p)}) · "
                    f"[Apple Maps]({apple_directions_url(lat, lng, p)}) · "
                    f"[View on Google Maps]({p['url']})"
                )

st.header("Tips for getting naloxone")
st.markdown(
    "- **Ask the pharmacist.** Narcan is sold over the counter, sometimes behind the counter. Just say \"I'd like naloxone.\"\n"
    "- **Call ahead** to check it's in stock and what it costs. Some insurance plans cover it.\n"
    "- **Free options:** many local health departments, harm reduction programs, libraries and community organizations give it away.\n"
    "- **Other places that may carry it:** hospitals, community health centers, treatment programs and some schools.\n"
    "- **Get two doses** and keep them together, somewhere others can find them."
)
