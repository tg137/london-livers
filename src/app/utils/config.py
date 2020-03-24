import configparser

config = configparser.ConfigParser()
config.read("config.ini")

BASE_URL = config["DEFAULT"]["BaseURL"]