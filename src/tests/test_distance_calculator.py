import unittest
from app.utils import distance_calculator


class TestDistanceCalculatorMethods(unittest.TestCase):
    def test_calculate_distance(self):
        # Two points roughly a mile away
        longitude1 = 51.389723
        latitude1 = -0.111998
        latitude2 = 51.377088
        longitude2 = -0.103045

        miles = distance_calculator.calculate_distance(latitude1, longitude1, latitude2, longitude2)

        # Assert that the two points are roughly a mile away from each other
        self.assertEqual(miles, 1, 1)


if __name__ == "__main__":
    unittest.main
