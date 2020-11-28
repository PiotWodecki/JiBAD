from CommonUtils import *

class Equation:

    @staticmethod
    def solve_equation(x_square_parameter, x_parameter, constant):
        try:
            # if float(x_parameter):
                if CommonUtils.is_float(x_square_parameter)and CommonUtils.is_float(x_parameter) \
                        and CommonUtils.is_float(constant):
                    #this if looks like this because after using float(x_parameter_ when x parameter equals 0 it return false
                    if x_square_parameter == 0:
                        if x_parameter == 0:
                            if constant == 0:
                                return ["Identity equation"]
                            else:
                                return []
                        else:
                            if x_parameter == 0:
                                raise ZeroDivisionError
                            else:
                                return [-constant / x_parameter]
                    else:
                            return Equation.calculate_roots(x_square_parameter, x_parameter, constant)
                else:
                    raise ValueError
        except ValueError:
            if x_parameter == 0:
                raise ZeroDivisionError
            else:
                return ["Incorrect input"]

        except ZeroDivisionError:
            return []

    @staticmethod
    def calculate_roots(x_square_parameter, x_parameter, constant):
        delta = x_parameter ** 2 - 4 * x_square_parameter * constant
        if delta > 0:
            return [(-x_parameter + delta ** 0.5) / (2 * x_square_parameter), (-x_parameter - delta ** 0.5) / (2 * x_square_parameter)]
        elif delta == 0:
            return [- x_parameter / (2 * x_square_parameter)]
        else:
            return []

    @staticmethod
    def display_equation(roots):
        try:
            if len(roots) > 2:
                raise IndexError
            if all(isinstance(x, (int, float)) for x in roots):
                if len(roots) == 0:
                    output = "There is no roots in real domain"
                elif len(roots) == 1:
                    output = "Two roots in the same position: " + str('{0:.2f}'.format(roots[0]))
                else:
                    output = "Root 1: " + str('{0:.2f}'.format(roots[0])) + "\nRoot 2: " + str('{0:.2f}'.format(roots[1]))
            else:
                raise ValueError

            return output

        except IndexError:
                return "Too many arguments"

        except ValueError:
            return "Arguments are not a numbers"


# print(Equation.display_equation([2, 5]))
# print(Equation.display_equation([-3]))
# print(Equation.display_equation([]))
# print(Equation.display_equation([2, 5, 7]))
# print(Equation.display_equation([2, "p"]))
