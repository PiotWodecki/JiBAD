class Polynomial:

    def __init__(self, factors):
        if factors is None:
            self.factors = []
        else:
            self.factors = factors

    def __repr__(self):
        degree_of_polynomial = len(self.factors)
        decrementor = degree_of_polynomial - 1
        characters_to_remove = ['+', '-']
        output = ""
        for i in range(degree_of_polynomial):
            if decrementor > 1:
                if self.factors[i] == 0:
                    pass
                else:
                    output += str(self.factors[i]) + 'x' + '^' + str(decrementor) + ' + '
            elif decrementor == 1:
                if self.factors[i] == 0:
                    pass
                else:
                    output += str(self.factors[i]) + 'x' + ' + '
            else:
                if self.factors[i] == 0:
                    pass
                else:
                    output += str(self.factors[i])
            decrementor -= 1

        output = output.strip()

        if len(output) > 0:
            if output[-1] in characters_to_remove:
                output = output[:-1]
        else:
            output = '0'

        output = output.strip()

        output = Polynomial.changing_sign(output)

        return output

    def __bool__(self):
        if all(factor == 0 for factor in self.factors) or self.factors is None:
            return False
        return True

    def find_integer_solution(self):
        p = Polynomial.find_divisors(self.factors[-1])
        q = Polynomial.find_divisors(self.factors[0])
        potential_solutions = [x/y for x in p for y in q]
        potential_solutions = list(set(potential_solutions))
        solutions = []
        for x in potential_solutions:
            if Polynomial.check_if_number_is_solution(self.factors, x) is True:
                solutions.append(x)
        print(solutions)
        return solutions

    def get_value(self, x):
        sum = 0
        help_poly = self.factors.copy()
        help_poly.reverse()
        for index, elem in enumerate(help_poly):
            sum += elem * (x ** index)

        return sum

    @staticmethod
    def check_if_number_is_solution(factors, number):
        sum = 0
        for index, x in enumerate(factors):
            sum += x*(number**index)
        if sum == 0:
            return True
        else:
            return False

    @staticmethod
    def find_divisors(number):
        divisors = []
        if number > 0:
            i = 1
            while i <= number:
                if number % i == 0:
                    divisors.append(i)
                    divisors.append(-i)
                i += 1
            return divisors

        if number < 0:
            i = -1
            while i >= number:
                if number % i == 0:
                    divisors.append(i)
                    divisors.append(-i)
                i -= 1
            return divisors

        return divisors


    @staticmethod
    def add_polynomials(polynomial1, polynomial2):
        sum = []
        if len(polynomial1.factors) == len(polynomial2.factors):
            sum = [polynomial1.factors[i] + polynomial2.factors[i] for i in range(len(polynomial1.factors))]
            return Polynomial(sum)
        else:
            Polynomial.complement_list(polynomial1, polynomial2)
            sum = [polynomial1.factors[i] + polynomial2.factors[i] for i in range(len(polynomial1.factors))]
            return Polynomial(sum)

    @staticmethod
    def subtraction_polynomials(polynomial1, polynomial2):
        subtraction = []
        if len(polynomial1.factors) == len(polynomial2.factors):
            subtraction = [polynomial1.factors[i] - polynomial2.factors[i] for i in range(len(polynomial1.factors))]
            return Polynomial(subtraction)
        else:
            Polynomial.complement_list(polynomial1, polynomial2)
            subtraction = [polynomial1.factors[i] - polynomial2.factors[i] for i in range(len(polynomial1.factors))]
            return Polynomial(subtraction)

    @staticmethod
    def multiplication_polynomials(polynomial1, polynomial2):
        factors_poly1 = polynomial1.factors.copy()
        factors_poly2 = polynomial2.factors.copy()
        factors_poly1.reverse()
        factors_poly2.reverse()
        multiplication = []

        multiplication = [[index1 + index2, (a*b)] for index1, a in enumerate(factors_poly1) for index2, b in enumerate(factors_poly2)]
        highest_degree = 0
        for item in multiplication:
            if item[0] > highest_degree:
                highest_degree = item[0]

        help_poly = []
        for i in range(highest_degree + 1):
            sum=0
            for item in multiplication:
                if item[0] == i:
                    sum += item[1]
            help_poly.append(sum)

        help_poly.reverse()

        return Polynomial(help_poly)


    @staticmethod
    def complement_list(polynomial1, polynomial2):
        length_gap = abs(len(polynomial1.factors) - len(polynomial2.factors))
        if len(polynomial1.factors) > len(polynomial2.factors):
            for i in range(length_gap):
                polynomial2.factors.insert(0, 0)
        else:
            for i in range(length_gap):
                polynomial1.factors.insert(0, 0)

    @staticmethod
    def changing_sign(polynomial_output):
        to_minus1 = '+ -'
        to_minus2 = '- +'
        to_plus1 = '+ +'
        to_plus2 = '- -'
        if to_minus1 in polynomial_output:
            polynomial_output = polynomial_output.replace(to_minus1, '-')
        if to_minus2 in polynomial_output:
            polynomial_output = polynomial_output.replace(to_minus2, '-')
        if to_plus1 in polynomial_output:
            polynomial_output = polynomial_output.replace(to_plus1, '+')
        if to_plus2 in polynomial_output:
            polynomial_output = polynomial_output.replace(to_plus2, '+')

        return polynomial_output


polynomial = Polynomial([2.5, 4, 5])
polynomial_empty = Polynomial([0 , 0, 0])
polynomial_empty2 = Polynomial([])
polynomial4 = Polynomial([2, 10, 7])
polynomial1 = Polynomial([5, 4, 3])
# print(polynomial)
# polynomial2 = Polynomial([-2, 10, 5, 0, 3])
# print(polynomial2)
# print(Polynomial.add_polynomials(polynomial, polynomial1))
# print(Polynomial.add_polynomials(polynomial, polynomial2))
# print()
# print(Polynomial.subtraction_polynomials(polynomial, polynomial2))
# print(Polynomial.subtraction_polynomials(polynomial, polynomial1))
# print(Polynomial.subtraction_polynomials(polynomial, polynomial2))
# print(Polynomial.subtraction_polynomials(polynomial, polynomial4))

print(Polynomial.multiplication_polynomials(polynomial, polynomial4))
print(bool(polynomial))
print(bool(polynomial_empty))
print(bool(polynomial_empty2))

print()
polynomial6 = Polynomial([1, 0, -1])
polynomial6.find_integer_solution()
print(polynomial6.get_value(5))


