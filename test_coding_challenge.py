import unittest
from coding_challenge_1 import get_term, get_yield, process, calculate_yield_spread
from mock import patch, MagicMock


# These tests are assuming that csv files never has blank values or fields
class TestCalculateYieldSpread(unittest.TestCase):
    # Testing diff values and result of get_term method
    def test_get_term(self):
        # Tests edge cases
        self.assertEqual(get_term('5.0 years'), 5.0)
        self.assertEqual(get_term('0 years'), 0)
        self.assertEqual(get_term('3 years'), 3.0)

    # Testing diff values and result of get_term method
    def test_get_yield(self):
        # Tests edge cases
        self.assertEqual(get_yield('5.0%'), 5.0)
        self.assertEqual(get_yield('0%'), 0)
        self.assertEqual(get_yield('3%'), 3.0)
        self.assertEqual(get_yield('3 %'), 3.0)


if __name__ == '__main__':
    unittest.main()
