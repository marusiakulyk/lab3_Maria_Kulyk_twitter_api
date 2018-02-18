import folium
from geopy.geocoders import Nominatim


def adding_marker(feature_group, location, popup):
    """
    This function adds marker on a map

    """
    geolocator = Nominatim()
    location1 = geolocator.geocode(location)
    feature_group.add_child(folium.Marker(location=[location1.latitude, location1.longitude],
                                          popup=popup,
                                          icon=folium.Icon()))


def map_creation(lst):
    map1 = folium.Map(location=[49.83, 24.014167],
                      zoom_start=5)

    fg = folium.FeatureGroup(name="followings")

    for i in lst:
        try:
            adding_marker(fg, i[-1], i[0] + "\n".join(i[1]))
        except AttributeError:
            continue
    map1.add_child(fg)
    map1.save(r"E:\Programming\lab2_02\lab\templates\Map.html")
