"""
Tests for the main module.
Uses mocking to simulate calls and responses to the external API.
"""

import unittest
import urllib
from unittest.mock import Mock, patch

import requests
import responses
from fastapi.testclient import TestClient

from app import main
from app.utils.config import BASE_URL, USERS_URL_SUFFIX, LONDON_USERS_URL_SUFFIX
from tests import test_users

CLIENT = TestClient(main.app)


def create_response(response_mocks, url_suffix: str, user_list: list, status_code: int):
    """
    Creates a mocked response with the information given in the args
    :param response_mocks: The response object to add the mock response to
    :param url_suffix: The URL suffix which needs to be mocked
    :param user_list: The user list that is to be returned in the mock
    :param status_code: The HTTP status code number to be used in the response
    """
    response_mocks.add(responses.GET, urllib.parse.urljoin(BASE_URL, url_suffix),
                       json=user_list, status=status_code)


class TestMainMethods(unittest.TestCase):
    @responses.activate
    def test_getting_user_that_lives_in_london_and_is_located_in_london(self):
        create_response(responses, LONDON_USERS_URL_SUFFIX, [test_users.london_live_and_located_user], 200)
        create_response(responses, USERS_URL_SUFFIX, [test_users.london_live_and_located_user], 200)

        response = CLIENT.get("users-in-london").json()

        # User should be in both lists
        self.assertEqual(len(response["living_in_london"]), 1)
        self.assertEqual(len(response["within_50_miles"]), 1)

    @responses.activate
    def test_getting_user_that_lives_in_london_but_is_not_located_there(self):
        create_response(responses, LONDON_USERS_URL_SUFFIX, [test_users.london_live_not_located_user], 200)
        create_response(responses, USERS_URL_SUFFIX, [test_users.london_live_not_located_user], 200)

        response = CLIENT.get("users-in-london").json()

        # User should be in the living_in_london list but not the within_50_miles list
        self.assertEqual(len(response["living_in_london"]), 1)
        self.assertEqual(len(response["within_50_miles"]), 0)

    @responses.activate
    def test_getting_user_that_doesnt_live_in_london_but_is_located_there(self):
        create_response(responses, LONDON_USERS_URL_SUFFIX, [], 200)
        create_response(responses, USERS_URL_SUFFIX, [test_users.london_located_not_live_user], 200)
        response = CLIENT.get("users-in-london").json()

        # User should be in the living_in_london list but not the within_50_miles list
        self.assertEqual(len(response["living_in_london"]), 0)
        self.assertEqual(len(response["within_50_miles"]), 1)

    @responses.activate
    def test_getting_user_that_doesnt_live_and_isnt_located_in_london(self):
        create_response(responses, LONDON_USERS_URL_SUFFIX, [], 200)
        create_response(responses, USERS_URL_SUFFIX, [test_users.not_located_or_living_in_london_user], 200)
        response = CLIENT.get("users-in-london").json()

        # User should be in the living_in_london list but not the within_50_miles list
        self.assertEqual(len(response["living_in_london"]), 0)
        self.assertEqual(len(response["within_50_miles"]), 0)

    @patch.object(main, "requests")
    def test_getting_from_the_external_api_when_it_is_down(self, mock_requests):
        mock_requests.exceptions = requests.exceptions
        mock_requests.get = Mock(side_effect=requests.exceptions.ConnectionError)
        response = CLIENT.get("users-in-london").json()

        # Should have received the correct error
        self.assertEqual(response.get("detail"), f"Could not access API at {BASE_URL}")

    @responses.activate
    def test_getting_from_the_external_api_and_getting_an_unexpected_response(self):
        create_response(responses, LONDON_USERS_URL_SUFFIX, [test_users.invalid_user], 200)
        create_response(responses, USERS_URL_SUFFIX, [test_users.invalid_user], 200)
        response = CLIENT.get("users-in-london").json()

        # Should have received the correct error
        self.assertEqual(response.get("detail"), f"API Response was not as expected from {BASE_URL}")

    @responses.activate
    def test_getting_from_the_external_api_and_empty_lists_are_returned(self):
        create_response(responses, "city/London/users", [], 200)
        create_response(responses, "users", [], 200)
        response = CLIENT.get("users-in-london").json()

        # Should have received empty lists
        self.assertEqual(response["living_in_london"], [])
        self.assertEqual(response["within_50_miles"], [])

    def test_getting_an_api_endpoint_that_doesnt_exist(self):
        response = CLIENT.get("unknown-endpoint").json()
        self.assertEqual(response["detail"], "Not Found")

    def test_executing_forbidden_method_on_endpoint(self):
        response = CLIENT.post("users-in-london").json()
        self.assertEqual(response["detail"], "Method Not Allowed")


if __name__ == "__main__":
    unittest.main
