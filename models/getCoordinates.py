from geopy.geocoders import Nominatim

class getCoordinates:
    def __init__(self) -> None:
        self.__geolocator = Nominatim(user_agent="getCoordinates")

    def get(self, a_str):
        location = self.__geolocator.geocode(a_str)
        if location == None:
            return None
        else:
            return [location.latitude, location.longitude]