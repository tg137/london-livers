"""
A module which holds a number of test users which can be used in mocked
responses when testing the API. Each user object is described by a comment above it.
The dictionaries mirror the response object which is retrieved from the external
API with some invalid responses thrown in there.
Specifying that users don't live in London is pointless in terms of logic as the API
works in such a way that a user simply won't be returned if they're not listed as living
in London. However, from a readability point of view, it makes sense to highlight this here.
"""

# A user that lives in London and who is located there
london_live_and_located_user = {
    "id": 1,
    "first_name": "user",
    "last_name": "one",
    "email": "user@one.com",
    "ip_address": "192.57.232.111",
    "latitude": 51.515168,
    "longitude": -0.176614
}

# A user that lives in London but isn't located there
london_live_not_located_user = {
    "id": 2,
    "first_name": "user",
    "last_name": "two",
    "email": "user@two.com",
    "ip_address": "192.57.232.111",
    "latitude": 25.995565,
    "longitude": -80.180822
}

# A user that is located in London but doesn't live there
london_located_not_live_user = {
    "id": 3,
    "first_name": "user",
    "last_name": "three",
    "email": "user@three.com",
    "ip_address": "192.57.232.111",
    "latitude": 51.515168,
    "longitude": -0.176614
}

# A user who neither lives nor is located in London
not_located_or_living_in_london_user = {
    "id": 4,
    "first_name": "user",
    "last_name": "four",
    "email": "user@four.com",
    "ip_address": "192.57.232.111",
    "latitude": 26.593819,
    "longitude": -80.098367
}

# An invalid user object
invalid_user = {
    "invalid": "field",
    "is": "invalid"
}