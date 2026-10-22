"""Server-side Google Geocoding and Places (New) calls. The API key never reaches the browser."""
from typing import Optional

import requests

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
NEARBY_URL = "https://places.googleapis.com/v1/places:searchNearby"
FIELDS = "places.id,places.displayName,places.formattedAddress,places.location,places.nationalPhoneNumber"
TIMEOUT = 10


class PlacesError(Exception):
    """A readable message that is safe to show to users (never contains the key)."""


def geocode(address: str, key: str) -> Optional[tuple]:
    """Return (lat, lng, formatted_address) for an address or ZIP, or None if nothing matched."""
    try:
        r = requests.get(GEOCODE_URL, params={"address": address, "key": key}, timeout=TIMEOUT)
        data = r.json()
    except (requests.RequestException, ValueError):
        raise PlacesError("Could not reach Google to look up that address. Try again in a moment.")
    status = data.get("status")
    if status == "ZERO_RESULTS":
        return None
    if status != "OK":
        raise PlacesError(f"Google Geocoding returned {status}: {data.get('error_message', 'no details')}")
    top = data["results"][0]
    loc = top["geometry"]["location"]
    return loc["lat"], loc["lng"], top.get("formatted_address", address)


def nearby_pharmacies(lat: float, lng: float, key: str, radius_m: int = 8000) -> list:
    """Return up to 20 nearby pharmacies as dicts: name, address, phone, lat, lng, url."""
    body = {
        "includedTypes": ["pharmacy", "drugstore"],
        "maxResultCount": 20,
        "locationRestriction": {"circle": {"center": {"latitude": lat, "longitude": lng}, "radius": float(radius_m)}},
    }
    headers = {"X-Goog-Api-Key": key, "X-Goog-FieldMask": FIELDS, "Content-Type": "application/json"}
    try:
        r = requests.post(NEARBY_URL, json=body, headers=headers, timeout=TIMEOUT)
        data = r.json()
    except (requests.RequestException, ValueError):
        raise PlacesError("Could not reach Google to find pharmacies. Try again in a moment.")
    if r.status_code != 200:
        err = data.get("error", {})
        raise PlacesError(f"Google Places returned {err.get('status', r.status_code)}: {err.get('message', 'no details')}")
    out = []
    for p in data.get("places", []):
        name = p.get("displayName", {}).get("text", "Pharmacy")
        loc = p.get("location", {})
        out.append({
            "name": name,
            "address": p.get("formattedAddress", ""),
            "phone": p.get("nationalPhoneNumber", ""),
            "lat": loc.get("latitude"),
            "lon": loc.get("longitude"),
            "url": "https://www.google.com/maps/search/?api=1&query=" + requests.utils.quote(f"{name} {p.get('formattedAddress', '')}")
                   + (f"&query_place_id={p['id']}" if p.get("id") else ""),
        })
    return [p for p in out if p["lat"] is not None and p["lon"] is not None]
