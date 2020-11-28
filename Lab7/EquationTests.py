import unittest
from Equation import *


class EquationTest(unittest.TestCase):

    def test_equation_return_type(self):
        self.assertIsInstance(Equation.solve_equation(1, 20, 3), list)
        self.assertIsInstance(Equation.solve_equation(0, 0, 0), list)
        self.assertIsInstance(Equation.solve_equation(2, 1, 3), list)
        self.assertIsInstance(Equation.solve_equation(1, 20, 3), list)
        self.assertIsInstance(Equation.solve_equation(1, 0, 3), list)
        self.assertIsInstance(Equation.solve_equation(0, 'p', 5), list)

    def test_equation(self):
        self.assertCountEqual(Equation.solve_equation(1, 1000, 3), [-0.0030000090000612545, -999.9969999909999])

    def test_parameters_equal_zero(self):
        self.assertEqual(Equation.solve_equation(0, 0, 0), ["Identity equation"])

    def test_x_square_parameter_equals_zero(self):
        self.assertEqual(Equation.solve_equation(0, 5, 10), [-2])
        self.assertEqual(Equation.solve_equation(0, 4, -2.5), [0.625])

    def test_both_x_parameters_equal_zero(self):
        self.assertEqual(Equation.solve_equation(0, 0, 5), [])
        self.assertEqual(Equation.solve_equation(0, 0, 100000), [])

    def test_x_parameter_equals_zero(self):
        self.assertEqual(Equation.solve_equation(2, 0, 5), [])
        self.assertEqual(Equation.solve_equation(3, 0, 5), [])

    def test_constant_equals_zero(self):
        self.assertCountEqual(Equation.solve_equation(2, 4, 0), [0, -2])
        self.assertCountEqual(Equation.solve_equation(3, -5.5, 0), [0, 1.8333333333333333])

    def test_different_roots(self):
        self.assertCountEqual(Equation.solve_equation(2, 10, 5), [-4.436491673103708, -0.5635083268962915])
        self.assertCountEqual(Equation.solve_equation(-5, -2, 10), [-1.6282856857085701, 1.22828568570857])
        self.assertCountEqual(Equation.solve_equation(-5.5, 2.5, 3), [-0.5454545454545454, 1])

    def test_one_root(self):
        self.assertEqual(Equation.solve_equation(1, 0, 0), [0])
        self.assertEqual(Equation.solve_equation(2, 4, 2), [-1])
        self.assertEqual(Equation.solve_equation(2, -4, 2), [1])

    def test_no_roots(self):
        self.assertEqual(Equation.solve_equation(0, 0, 5), [])
        self.assertEqual(Equation.solve_equation(2, 1, 5.25), [])

    def test_no_valid_parameters(self):
        self.assertRaises(ValueError)
        self.assertEqual(Equation.solve_equation(0, 'p', 5), ["Incorrect input"])

    def test_display_equation_for_valid_arguments(self):
        test = "Valid arguments - 2 roots"
        expect = "Root 1: 1.00\nRoot 2: -1.00"
        failure_msg = 'display_equation({0}) should return {1} but returned {2}'
        actual = Equation.display_equation([1, -1])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

        test = "Valid arguments - 1 root"
        expect = "Two roots in the same position: -3.00"
        failure_msg = 'display_equation({0}) should return {1} but returned {2}'
        actual = Equation.display_equation([-3])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

        test = "Valid arguments - no roots"
        expect = "There is no roots in real domain"
        failure_msg = 'display_equation({0}) should return {1} but returned {2}'
        actual = Equation.display_equation([])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

    def test_display_equation_for_not_valid_arguments(self):
        test = "String argument"
        expect = "Arguments are not a numbers"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = Equation.display_equation(["p", 2])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))

        test = "Too many arguments"
        expect = "Too many arguments"
        failure_msg = 'print_linear_expression({0}) should return {1} but returned {2}'
        actual = Equation.display_equation([0, 2, 3])
        self.assertEqual(expect, actual, failure_msg.format(test, expect, actual))


if __name__ == "__main__":
    unittest.main()
