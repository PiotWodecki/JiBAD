import unittest

from EquationTests import *
from LinearExpressionTests import *
from CommonUtilsTests import *


def main():
    try:
        print("Podaj współczynniki równania:")
        a, b, c = CommonUtils.get_three_numbers()
        roots = Equation.solve_equation(a, b, c)
        print(Equation.display_equation(roots))

        print("Podaj dwa punkty:")
        x1, y1, x2, y2 = CommonUtils.get_two_points()
        linear_expression = LinearExpression.determine_straight_line(x1, y1, x2, y2)
        print(LinearExpression.display_linear_expression(linear_expression))

    except ValueError:
        print("Input is incorrect")

    print()
    print("Check tests: ")
    unittest.main()


if __name__=="__main__":
    main()