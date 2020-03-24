import urllib

from fastapi import FastAPI, HTTPException
import requests
from app.utils.config import BASE_URL, LONDON_USERS_URL_SUFFIX, USERS_URL_SUFFIX

app = FastAPI()


@app.get("/users-in-london")
def get_users_in_london():
    # Get the users who live in London
    city_url = urllib.parse.urljoin(BASE_URL, LONDON_USERS_URL_SUFFIX)
    city_response = requests.get(city_url)

    # Get the full list of users
    users_url = urllib.parse.urljoin(BASE_URL, USERS_URL_SUFFIX)
    users_response = requests.get(users_url)

    response = {"living_in_london": city_response.json(), "within_50_miles": users_response.json()}
    return response
