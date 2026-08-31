import os
from pathlib import Path

import geocoder
import requests
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

ors_api = os.getenv("ORS_API_KEY")
REQUEST_TIMEOUT = 10

def get_current_location():
    """it will get an approximate location from the internet connection"""
    try:
        location = geocoder.ip("me")

        if location.ok and location.latlng:
            return location.latlng

        print("Could not find an approximate location")

    except Exception as error:
        print(f"Location error: {error}")

    return None

def get_directions(destination):
    """it finds the directions to the destination."""
    if not ors_api:
        return None, "ORS_API_KEY is missing from the .env file"

    if not isinstance(destination, str) or not destination.strip():
        return None, "No destination was provided"

    destination = destination.strip()
    origin = get_current_location()

    if not origin:
        return None, "Could not get your approximate location"

    try:
        geocode_response = requests.get(
            "https://api.openrouteservice.org/geocode/search",
            params={
                "api_key": ors_api,
                "text": destination,
                "size": 1,
            },
            timeout=REQUEST_TIMEOUT,
        )
        geocode_response.raise_for_status()

        places = geocode_response.json().get("features", [])

        if not places:
            return None, f"Could not find {destination}"

        place = places[0]
        dest_coords = place["geometry"]["coordinates"]
        dest_name = place["properties"].get("label", destination)

        route_response = requests.post(
            "https://api.openrouteservice.org/v2/directions/driving-car",
            headers={"Authorization": ors_api},
            json={
                "coordinates": [
                    [origin[1], origin[0]],
                    [dest_coords[0], dest_coords[1]],
                ]
            },
            timeout=REQUEST_TIMEOUT,
        )
        route_response.raise_for_status()

        routes = route_response.json().get("routes", [])

        if not routes:
            return None, "Could not get directions"

        route = routes[0]
        segments = route.get("segments", [])

        if not segments:
            return None, "The route has no directions"

        steps = segments[0].get("steps", [])

        directions = [
            {
                "instruction": step.get("instruction", ""),
                "distance": round(step.get("distance", 0)),
            }
            for step in steps[:5]
        ]

        summary = route.get("summary", {})
        distance_km = round(summary.get("distance", 0) / 1000, 1)
        time_minutes = round(summary.get("duration", 0) / 60)

        return (
            directions,
            f"Route to {dest_name} — "
            f"{distance_km} km, {time_minutes} mins",
        )

    except requests.RequestException:
        return None, "The navigation service could not be reached"

    except (KeyError, TypeError, ValueError):
        return None, "The navigation service returned invalid data"

def parse_nav_command(text):
    """
    it gets the destination from a spoken navigation command 
    like navigate to the nearest petrol pump
    """
    if not isinstance(text, str):
        return None

    original_text = text.strip()
    lower_text = original_text.lower()

    commands = (
        "navigate to",
        "go to",
        "take me to",
        "directions to",
        "how do i get to",
        "put a map to",
        "show me the way to",
        "route to",
        "get me to",
        "find a route to",
    )

    for command in commands:
        position = lower_text.find(command)

        if position != -1:
            destination = original_text[position + len(command):].strip()
            return destination or None

    return None