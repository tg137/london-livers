import configparser

config = configparser.ConfigParser()
config.read("config.ini")

BASE_URL = config["DEFAULT"]["BaseURL"]
EARTH_RADIUS = config.getfloat("DEFAULT", "EarthRadius")
KILOMETRES_TO_MILES_CONVERSION_FACTOR = config.getfloat("DEFAULT", "KilometresToMilesFactor")
LONDON_LATITUDE = config.getfloat("DEFAULT", "LondonLatitude")
LONDON_LONGITUDE = config.getfloat("DEFAULT", "LondonLongitude")
