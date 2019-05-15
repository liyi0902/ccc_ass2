from geopy.geocoders import Nominatim
geolocator = Nominatim()
location = geolocator.reverse("-37.8811,145.0969")
print(location.raw["address"]["suburb"])
# Chadstone
