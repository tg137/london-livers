"""
The config module reads the config parameters in from the config.ini file
and exposes them as variables that can be imported into other modules.
"""

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

BASE_URL = config["DEFAULT"]["BaseURL"]
USERS_URL_SUFFIX = config["DEFAULT"]["UsersUrlSuffix"]
LONDON_USERS_URL_SUFFIX = config["DEFAULT"]["UsersInLondonUrlSuffix"]

EARTH_RADIUS = config.getfloat("DEFAULT", "EarthRadius")
KILOMETRES_TO_MILES_CONVERSION_FACTOR = config.getfloat("DEFAULT", "KilometresToMilesFactor")
LONDON_LATITUDE = config.getfloat("DEFAULT", "LondonLatitude")
LONDON_LONGITUDE = config.getfloat("DEFAULT", "LondonLongitude")
