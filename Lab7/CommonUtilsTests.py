import unittest
from unittest.mock import patch
from CommonUtils import *


class CommonUtilsTest(unittest.TestCase):

    @patch('builtins.input', side_effect = ['2', '3.5', '-20'])
    def test_user_input_valid_arguments_three_numbers(self, params):
        self.assertEqual(CommonUtils.get_three_numbers(), [2, 3.5, -20])

    @patch('builtins.input', side_effect = ['2', 'string', '2,2'])
    def test_user_input_not_valid_arguments_three_numbers(self, params):
        self.assertRaises(ValueError)

    @patch('builtins.input', side_effect=['2', '2.5', '-10', '24'])
    def test_user_valid_input_two_points(self, params):
        self.assertEqual(CommonUtils.get_two_points(), [2, 2.5, -10, 24])

    @patch('builtins.input', side_effect=['2', 'impostor', ',', '24'])
    def test_user_valid_input_two_points(self, params):
        self.assertRaises(ValueError)

    def test_is_float_function(self):
        self.assertTrue(CommonUtils.is_float(1))
        self.assertTrue(CommonUtils.is_float(0.33))
        self.assertTrue(CommonUtils.is_float(-0.33))
        self.assertFalse(CommonUtils.is_float('p'))
        self.assertFalse(CommonUtils.is_float("chillwagon"))


if __name__ == "__main__":
    unittest.main()