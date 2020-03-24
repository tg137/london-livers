from math import sin, cos, sqrt, atan2, radians
from app.utils.config import EARTH_RADIUS, KILOMETRES_TO_MILES_CONVERSION_FACTOR, LONDON_LONGITUDE, LONDON_LATITUDE


def calculate_distance(lat1: float, long1: float, lat2: float, long2: float) -> float:
    """
    Calculates the distance in miles between two lat/long coordinate points
    :param lat1: The latitude of the first coordinate point
    :param long1: The longitude of the first coordinate point
    :param lat2: The latitude of the second coordinate point
    :param long2: The longitude of the second coordinate point
    :return distance: The distance between the two points in miles
    """
    # Convert the latitude and longitudes to be in Radians
    lat1 = radians(lat1)
    long1 = radians(long1)
    lat2 = radians(lat2)
    long2 = radians(long2)

    # Get individual distances for latitude and longitude
    dlat = lat2 - lat1
    dlong = long2 - long1

    distance = _haversine_formula(dlat, lat1, lat2, dlong)
    return _kilometres_to_miles(distance)


def calculate_distance_to_london(latitude: float, longitude: float) -> float:
    """
    Calculates the distance from a given coordinate point to the centre of London
    :param latitude: The latitude of the given coordinate point
    :param longitude: The longitude of the given coordinate point
    :return distance: The distance between the point and London in miles
    """
    return calculate_distance(latitude, longitude, LONDON_LATITUDE, LONDON_LONGITUDE)


def _haversine_formula(dlat: float, lat1: float, lat2: float, dlon: float) -> float:
    """
    The Haversine formula which determines the great-circle distance between two points
    :param dlat: The delta of the two latitude values
    :param lat1: The latitude of the first set of coordinates
    :param lat2: The latitude of the second set of coordinates
    :param dlon: The delta of the two longitude values
    :return distance: The distance between the two points in kilometres
    """
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = EARTH_RADIUS * c
    return EARTH_RADIUS * c


def _kilometres_to_miles(kilometres: float) -> float:
    """
    :param kilometres: The value in kilometres that needs to be converted to miles
    :return miles: The value in miles
    """
    return kilometres * KILOMETRES_TO_MILES_CONVERSION_FACTOR
