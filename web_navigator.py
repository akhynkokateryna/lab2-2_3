"web_navigator.py"

import folium
from geopy import Nominatim
import twitter2

def user_locations(data):
    "Creates dictionary with user names and their locations"
    res = dict()
    for user in data['users']:
        if len(user['location']) == 0:
            continue
        res[user['screen_name']] = user['location']
    return res


def coordinates(locations, geolocator):
    "Transforms user locations into coordinates"
    for loc in locations:
        coord = geolocator.geocode(locations[loc], timeout = None)
        if coord is None:
            continue
        locations[loc] = (coord.latitude, coord.longitude)
    return locations


def main(name):
    data = twitter2.get_data(name)
    location = user_locations(data)
    geolocator1 = Nominatim(user_agent="web_navigator.py")
    coords = coordinates(location, geolocator1)

    new_map = folium.Map()

    layer = folium.FeatureGroup(name="friends locations")
    for loc in coords:
        try:
            new_map.add_child(layer.add_child(folium.Marker(location=[coords[loc][0], \
            coords[loc][1]], popup=loc)))
        except ValueError:
            continue

    new_map.save('mysite/templates/new_map.html')
