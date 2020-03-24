"""
Tests for the distance calculator module
"""

import unittest
from app.utils import distance_calculator


class TestDistanceCalculatorMethods(unittest.TestCase):
    def test_calculate_distance(self):
        # Two points roughly a mile away from each other
        latitude1 = 51.389723
        longitude1 = -0.111998
        latitude2 = 51.377088
        longitude2 = -0.103045

        miles = distance_calculator.calculate_distance(latitude1, longitude1, latitude2, longitude2)

        # Assert that the two points are roughly a mile away from each other
        self.assertAlmostEqual(miles, 1, 1)

    def test_kilometres_to_miles_conversion(self):
        # Roughly a mile in kilometres
        kilometres = 1.609347087886444
        miles = distance_calculator._kilometres_to_miles(kilometres)
        self.assertAlmostEqual(miles, 1)

    def test_calculate_distance_to_london(self):
        # A point in Leipzig, approximately 538 miles from London
        latitude = 51.339810
        longitude = 12.378256

        miles = distance_calculator.calculate_distance_to_london(latitude, longitude)

        # Asset that the two points are approximately 538 miles from each other
        self.assertAlmostEqual(miles, 538, 1)


if __name__ == "__main__":
    unittest.main
