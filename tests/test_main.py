import unittest
from main import find_lowest_price, calculate_total_price, load_json


class TestMainFunctions(unittest.TestCase):

    def test_find_lowest_price(self):
        shown_prices = {
            "King Studio Suite - Hearing Accessible/Non-Smoking": "113.05",
            "King Studio Suite - Non Smoking": "90",
            "King Room - Mobility/Hearing Accessible - Non-Smoking": "115.05",
            "Queen Suite with Two Queen Beds - Non-Smoking": "112.05",
        }
        lowest_price, lowest_price_room_type = find_lowest_price(shown_prices)
        self.assertEqual(lowest_price, 90)
        self.assertEqual(lowest_price_room_type, "King Studio Suite - Non Smoking")

    def test_calculate_total_price(self):
        net_prices = {
            "King Studio Suite - Hearing Accessible/Non-Smoking": "113.05",
            "King Studio Suite - Non Smoking": "90",
        }
        taxes = {"TAX": "14.70", "City tax": "4.01"}
        total_prices = calculate_total_price(net_prices, taxes)
        self.assertAlmostEqual(
            total_prices["King Studio Suite - Hearing Accessible/Non-Smoking"],
            131.76,
            places=2,
        )
        self.assertAlmostEqual(
            total_prices["King Studio Suite - Non Smoking"], 108.71, places=2
        )

    def test_load_json(self):
        data = load_json("Python-task.json")
        self.assertIn("assignment_results", data)
        self.assertIsInstance(data, dict)


if __name__ == "__main__":
    unittest.main()
