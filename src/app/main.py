import urllib

from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

BASE_URL = "https://bpdts-test-app.herokuapp.com"


@app.get("/users-in-london")
def get_users_in_london():
    # Get the users who live in London
    city_url = urllib.parse.urljoin(BASE_URL, "city/London/users")
    city_response = requests.get(city_url)

    # Get the full list of users
    users_url = urllib.parse.urljoin(BASE_URL, "users")
    users_response = requests.get(users_url)

    response = {"living_in_london": city_response.json(), "within_50_miles": users_response.json()}
    return response
