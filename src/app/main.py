import json
import urllib

import requests
from fastapi import FastAPI, HTTPException

from app.utils.config import BASE_URL, LONDON_USERS_URL_SUFFIX, USERS_URL_SUFFIX
from app.utils.distance_calculator import calculate_distance_to_london

app = FastAPI()


@app.get("/users-in-london")
def get_users_in_london():
    try:
        # Get the users who live in London
        city_url = urllib.parse.urljoin(BASE_URL, LONDON_USERS_URL_SUFFIX)
        city_response = requests.get(city_url)

        # Get the full list of users
        users_url = urllib.parse.urljoin(BASE_URL, USERS_URL_SUFFIX)
        users_response = requests.get(users_url)

        # Use list comprehension to add users to the response if their distance to London is less than 50 miles
        within_50_miles = [user for user in users_response.json()
                           if calculate_distance_to_london(
                               float(user["latitude"]),
                               float(user["longitude"])
                           ) < 50]

        # Split the response into two segments: one for those living in London, one for those within 50 miles
        response = {"living_in_london": city_response.json(), "within_50_miles": within_50_miles}
        return response

    except requests.exceptions.ConnectionError:
        raise HTTPException(status_code=500, detail=f"Could not access API at {BASE_URL}")
    except (KeyError, json.decoder.JSONDecodeError):
        raise HTTPException(status_code=500, detail=f"API Response was not as expected from {BASE_URL}")
