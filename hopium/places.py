"""Server-side Google Geocoding and Places (New) calls. The API key never reaches the browser."""
from typing import Optional

import requests

GEOCODE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
NEARBY_URL = "https://places.googleapis.com/v1/places:searchNearby"
FIELDS = "places.id,places.displayName,places.formattedAddress,places.location,places.nationalPhoneNumber,places.primaryType"
PHARMACY_TYPES = ("pharmacy", "drugstore")
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
        "includedPrimaryTypes": list(PHARMACY_TYPES),
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
        # Belt and braces: keep only places whose main business is a pharmacy (drops dollar stores, groceries, etc.).
        if p.get("primaryType") not in PHARMACY_TYPES:
            continue
        name = p.get("displayName", {}).get("text", "Pharmacy")
        loc = p.get("location", {})
        out.append({
            "id": p.get("id", ""),
            "name": name,
            "address": p.get("formattedAddress", ""),
            "phone": p.get("nationalPhoneNumber", ""),
            "lat": loc.get("latitude"),
            "lon": loc.get("longitude"),
            "url": "https://www.google.com/maps/search/?api=1&query=" + requests.utils.quote(f"{name} {p.get('formattedAddress', '')}")
                   + (f"&query_place_id={p['id']}" if p.get("id") else ""),
        })
    return [p for p in out if p["lat"] is not None and p["lon"] is not None]


def directions_url(origin_lat: float, origin_lng: float, place: dict) -> str:
    """Google Maps turn-by-turn directions from the searched location to a pharmacy (no API key needed)."""
    q = requests.utils.quote
    url = (f"https://www.google.com/maps/dir/?api=1&origin={origin_lat},{origin_lng}"
           f"&destination={q(place['name'] + ' ' + place['address'])}&travelmode=driving")
    return url + (f"&destination_place_id={place['id']}" if place.get("id") else "")


def apple_directions_url(origin_lat: float, origin_lng: float, place: dict) -> str:
    return (f"https://maps.apple.com/?saddr={origin_lat},{origin_lng}"
            f"&daddr={requests.utils.quote(place['name'] + ' ' + place['address'])}&dirflg=d")
