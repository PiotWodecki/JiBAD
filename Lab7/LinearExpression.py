from CommonUtils import *

class LinearExpression:

    @staticmethod
    def determine_straight_line(first_point_x, first_point_y, second_point_x, second_point_y):
        try:
            if CommonUtils.is_float(first_point_x) and CommonUtils.is_float(first_point_y) \
                    and CommonUtils.is_float(second_point_x) and CommonUtils.is_float(second_point_y):
                # this if looks like this because after using float(x_parameter_ when x parameter equals 0 it return false
                if first_point_x == second_point_x and first_point_y == second_point_y:
                    raise ZeroDivisionError
                a = (first_point_y - second_point_y) / (first_point_x - second_point_x)
                b = first_point_y - ((first_point_y - second_point_y) / (first_point_x - second_point_x) * first_point_x)
                return [a, b]
            else:
                raise ValueError

        except ZeroDivisionError:
            if first_point_y != second_point_y:
                return ["Cannot create a function from this points"]    # Przez punkty (1,0) i (1,1) nie biegnie prosta?
            else:
                return ["Two identical points - it is impossible to create linear expression"]
        except ValueError:
            return ["Incorrect argument"]

    @staticmethod
    def display_linear_expression(equation_rates):
        output = "y = "
        try:
            if len(equation_rates) != 2:
                raise IndexError
            if all(isinstance(x, (int,float)) for x in equation_rates):
                if equation_rates[0] != 0:
                    if equation_rates[1] > 0:
                        output += str(float(equation_rates[0])) + 'x ' + '+ ' + str(float(equation_rates[1]))
                    elif equation_rates[1] == 0:
                        output += str(float(equation_rates[0])) + 'x'
                    else:
                        output += str(float(equation_rates[0])) + 'x ' + '- ' + str(abs(float(equation_rates[1])))
                else:
                    output += str(float(equation_rates[1]))
            else:
                raise ValueError

            return output

        except IndexError:
            return "Too many arguments"

        except ValueError:
            return "Arguments are not a numbers"


# LinearExpression.print_linear_expression([0, 5])
# LinearExpression.print_linear_expression([2, -5])
# LinearExpression.print_linear_expression([-2.25, 0])
# LinearExpression.print_linear_expression([0, 0])
