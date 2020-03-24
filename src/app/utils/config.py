import configparser

config = configparser.ConfigParser()
config.read("config.ini")

BASE_URL = config["DEFAULT"]["BaseURL"]
EARTH_RADIUS = config.getfloat("DEFAULT", "EarthRadius")
KILOMETRES_TO_MILES_CONVERSION_FACTOR = config.getfloat("DEFAULT", "KilometresToMilesFactor")