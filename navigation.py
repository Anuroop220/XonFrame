import requests
import geocoder

ORS_API_KEY = "eyJvcmciOiI1YjNjZTM1OTc4NTExMTAwMDFjZjYyNDgiLCJpZCI6IjBkMmNiZmQ2ODBlMDQ2ZDdhOWNiYTgzMWQ1MTNkMWRjIiwiaCI6Im11cm11cjY0In0="

def get_current_location():
    g = geocoder.ip('me')
    if g.ok:
        return g.latlng
    return None

def get_directions(destination):
    try:
        # Get current location
        origin = get_current_location()
        if not origin:
            return None, "Could not get your location"

        # Geocode destination
        geo_url = "https://api.openrouteservice.org/geocode/search"
        geo_params = {
            "api_key": ORS_API_KEY,
            "text": destination,
            "size": 1
        }
        geo_response = requests.get(geo_url, params=geo_params).json()
        
        if not geo_response["features"]:
            return None, f"Could not find {destination}"
        
        dest_coords = geo_response["features"][0]["geometry"]["coordinates"]
        dest_name = geo_response["features"][0]["properties"]["label"]

        # Get route
        route_url = "https://api.openrouteservice.org/v2/directions/driving-car"
        headers = {"Authorization": ORS_API_KEY}
        body = {
            "coordinates": [
                [origin[1], origin[0]],
                [dest_coords[0], dest_coords[1]]
            ]
        }
        
        route_response = requests.post(route_url, json=body, headers=headers).json()
        
        if "routes" not in route_response:
            return None, "Could not get directions"
        
        route = route_response["routes"][0]
        steps = route["segments"][0]["steps"]
        
        directions = []
        for step in steps[:5]:
            instruction = step["instruction"]
            distance = round(step["distance"])
            directions.append({
                "instruction": instruction,
                "distance": distance
            })
        
        total_distance = round(route["summary"]["distance"] / 1000, 1)
        total_time = round(route["summary"]["duration"] / 60)
        
        return directions, f"Route to {dest_name} — {total_distance}km, {total_time} mins"
    
    except Exception as e:
        return None, f"Navigation error: {str(e)}"

def parse_nav_command(text):
    keywords = ["navigate to", "go to", "take me to", "directions to", "how do i get to", "put a map to"]
    for keyword in keywords:
        if keyword in text.lower():
            destination = text.lower().split(keyword)[-1].strip()
            return destination
    return None