import json
import os

import streamlit as st
import streamlit.components.v1 as components

st.title("Find Narcan near you")


def api_key() -> str:
    try:
        return st.secrets["GOOGLE_MAPS_API_KEY"]
    except Exception:
        return os.environ.get("GOOGLE_MAPS_API_KEY", "")


key = api_key()
if not key:
    st.info(
        "The map needs a Google Maps API key. Add `GOOGLE_MAPS_API_KEY` to `.streamlit/secrets.toml` "
        "(see `.streamlit/secrets.toml.example`) or set it as an environment variable, then restart the app. "
        "Enable **Maps JavaScript API** and **Places API (New)** and restrict the key to your site's URL."
    )
    st.stop()

PAGE = """
<style>
  body { margin:0; font-family: system-ui, sans-serif; }
  #bar { display:flex; gap:8px; margin-bottom:8px; }
  #addr { flex:1; padding:8px; border:1px solid #9ab; border-radius:8px; }
  button { padding:8px 14px; border:0; border-radius:8px; background:#1f3b57; color:#fff; cursor:pointer; }
  #map { height:420px; border-radius:12px; }
  #list { margin-top:10px; }
  .row { background:#fff; border:1px solid #bfe3f7; border-radius:10px; padding:8px 12px; margin-bottom:6px; }
  .row small { color:#456; }
</style>
<div id="bar"><input id="addr" placeholder="Enter an address or ZIP (or allow location)"><button id="go">Search</button></div>
<div id="map"></div><div id="list"></div>
<script>
(g=>{var h,a,k,p="The Google Maps JavaScript API could not load.",c="google",l="importLibrary",q="__ib__",m=document,b=window;b=b[c]||(b[c]={});var d=b.maps||(b.maps={}),r=new Set,e=new URLSearchParams,u=()=>h||(h=new Promise(async(f,n)=>{await (a=m.createElement("script"));e.set("libraries",[...r]+"");for(k in g)e.set(k.replace(/[A-Z]/g,t=>"_"+t[0].toLowerCase()),g[k]);e.set("callback",c+".maps."+q);a.src=`https://maps.${c}apis.com/maps/api/js?`+e;d[q]=f;a.onerror=()=>h=n(Error(p));a.nonce=m.querySelector("script[nonce]")?.nonce||"";m.head.append(a)}));d[l]?console.warn(p+" Only loads once."):d[l]=(f,...n)=>r.add(f)&&u().then(()=>d[l](f,...n))})({key:__KEY__,v:"weekly"});

const DEFAULT = {lat: 39.5, lng: -98.35};
let map, markers = [];
async function init() {
  const {Map} = await google.maps.importLibrary("maps");
  map = new Map(document.getElementById("map"), {center: DEFAULT, zoom: 4});
  document.getElementById("go").onclick = geocode;
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      p => search({lat: p.coords.latitude, lng: p.coords.longitude}),
      () => { document.getElementById("list").textContent = "Location blocked. Enter an address above."; });
  }
}
async function geocode() {
  const {Geocoder} = await google.maps.importLibrary("geocoding");
  const r = await new Geocoder().geocode({address: document.getElementById("addr").value});
  if (r.results[0]) search(r.results[0].geometry.location.toJSON());
}
async function search(center) {
  const {Place} = await google.maps.importLibrary("places");
  const {AdvancedMarkerElement} = await google.maps.importLibrary("marker");
  markers.forEach(m => m.map = null); markers = [];
  map.setCenter(center); map.setZoom(13);
  const {places} = await Place.searchNearby({
    fields: ["displayName", "formattedAddress", "location", "nationalPhoneNumber"],
    locationRestriction: {center, radius: 8000},
    includedPrimaryTypes: ["pharmacy", "drugstore"],
    maxResultCount: 20,
  });
  const list = document.getElementById("list");
  list.innerHTML = places.length ? "" : "No pharmacies found nearby.";
  const info = new google.maps.InfoWindow();
  places.forEach(p => {
    const m = new AdvancedMarkerElement({map, position: p.location, title: p.displayName});
    m.addListener("click", () => { info.setContent("<b>"+p.displayName+"</b><br>"+(p.formattedAddress||"")); info.open(map, m); });
    markers.push(m);
    const d = document.createElement("div"); d.className = "row";
    d.innerHTML = "<b></b><br><small></small>";
    d.querySelector("b").textContent = p.displayName;
    d.querySelector("small").textContent = (p.formattedAddress||"") + (p.nationalPhoneNumber ? " · " + p.nationalPhoneNumber : "");
    list.append(d);
  });
}
init();
</script>
"""

st.caption(
    "Most U.S. pharmacies can dispense naloxone, but stock varies. Google does not show whether Narcan "
    "is on the shelf, so call ahead to confirm."
)
components.html(PAGE.replace("__KEY__", json.dumps(key)), height=760, scrolling=True)
