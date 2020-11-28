import unittest

from LinearExpression import *


class LinearExpressionTests(unittest.TestCase):

    def test_return_type(self):
        self.assertIsInstance(LinearExpression.determine_straight_line(0, 0, 1, 1), list)
        self.assertIsInstance(LinearExpression.determine_straight_line(2, 4.5, -3, -2), list)
        self.assertIsInstance(LinearExpression.determine_straight_line(-2, -4.5, 3, 2), list)
        self.assertIsInstance(LinearExpression.determine_straight_line(0, -5, 0, -5), list)

    def test_determine_valid_straight_line(self):
        self.assertEqual(LinearExpression.determine_straight_line(0, 0, 1, 1), [1, 0])
        self.assertEqual(LinearExpression.determine_straight_line(2, 4.5, -3, -2), [1.3, 1.9])
        self.assertEqual(LinearExpression.determine_straight_line(-2, -4.5, 3, 2), [1.3, -1.9])

    def test_two_identical_points(self):
        self.assertEqual(LinearExpression.determine_straight_line(0, -5, 0, -5),
                         ["Two identical points - it is impossible to create linear expression"])
        self.assertEqual(LinearExpression.determine_straight_line(1000000, -302.5, 1000000, -302.5),
                         ["Two identical points - it is impossible to create linear expression"])

    def test_constant_function(self):
        self.assertEqual(LinearExpression.determine_straight_line(0, 1, 1, 1), [0, 1])
        self.assertEqual(LinearExpression.determine_straight_line(-100, 2.25, 12, 2.25), [0, 2.25])
        self.assertEqual(LinearExpression.determine_straight_line(-0.3333, -12, 0.6666, -12), [0, -12])

    def test_identical_x(self):
        self.assertEqual(LinearExpression.determine_straight_line(1, 1, 1, -1),
                         ["Cannot create a function from this points"])
        self.assertEqual(LinearExpression.determine_straight_line(-100, 0, -100, 2.25),
                         ["Cannot create a function from this points"])
        self.assertEqual(LinearExpression.determine_straight_line(-0.3333, 100, -0.3333, -12),
                         ["Cannot create a function from this points"])

    def test_incorrect_input(self):
        self.assertEqual(LinearExpression.determine_straight_line(1, 'jibad', 1, -1),
                         ["Incorrect argument"])
        self.assertEqual(LinearExpression.determine_straight_line(-100, 12, 'impostor', 2.25),
                         ["Incorrect argument"])

    def test_display_linear_expression_for_valid_arguments(self):
        test = "y = 0"
        expect = "y = 0.0"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = LinearExpression.display_linear_expression([0, 0])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

        test = "Correct arguments - ints"
        expect = "y = 1.0x + 1.0"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = LinearExpression.display_linear_expression([1, 1])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

        test = "Correct arguments"
        expect = "y = -12.33x - 82.4"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = LinearExpression.display_linear_expression([-12.33, -82.4])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

    def test_display_linear_expression_for_not_valid_arguments(self):
        test = "String argument"
        expect = "Arguments are not a numbers"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = LinearExpression.display_linear_expression(['p', -82.4])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

        test = "Too many arguments"
        expect = "Too many arguments"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = LinearExpression.display_linear_expression([12, -82.4, 16])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))


if __name__ == "__main__":
    unittest.main()