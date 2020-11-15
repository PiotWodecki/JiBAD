import string


class Automat:

    def __init__(self):
        self.state = "q0"
        self.counter = 0

    def check_correctness(self, expression):
        expression = expression.replace(" ", "")
        if self.is_string_acceptable(expression):
            for element in expression:
                if self.state == "q0":
                    self.state_q0_handler(element)
                elif self.state == "q1":
                    self.state_q1_handler(element)
                else:
                    self.state = "Reject"
        if self.state == "q1" and self.counter == 0:
            return True
        else:
            return False

    def state_q0_handler(self, character):
        if character == '(':
            self.state = "q0"
            self.counter = self.counter + 1
        elif character == '~':
            self.state = "q0"
        elif character in set(string.ascii_lowercase) or character == '1' or character == '0':
            self.state = "q1"
        else:
            self.state = "Reject"

    def state_q1_handler(self, character):
        if character == ')':
            self.state = "q1"
            self.counter = self.counter - 1
        elif character == '&' or character == '|':
            self.state = "q0"
        else:
            self.state = "Reject"

    def is_string_acceptable(self, value):
        allowed = set(string.ascii_lowercase + '0' + '1' + '|' + '&' + '~' + '(' + ')')
        if any((c not in allowed) for c in value):
            return False
        else:
            return True

    def set_to_begin_state(self):
        self.state = "q0"
        self.counter = 0

    def check_expression(self, expression):
        self.set_to_begin_state()
        if self.check_correctness(expression):
            return True
        else:
            return False

automat = Automat()
print("Prawdziwe: ")
print(automat.check_expression("~~a|b"))
print(automat.check_expression("a"))
print(automat.check_expression("a|b"))
print(automat.check_expression("a & b | a"))
print(automat.check_expression("(a &b) |c&~d"))
print(automat.check_expression("~~a"))
print(automat.check_expression("~(a|c)"))
print(automat.check_expression("(a)"))
print(automat.check_expression("((((a))))"))
print()
print("Nieprawdziwe:")
print(automat.check_expression("~"))
print(automat.check_expression("a|"))
print(automat.check_expression("A|B"))
print(automat.check_expression("a|&b"))
print(automat.check_expression("b~"))
print(automat.check_expression("(a|b"))
print(automat.check_expression("a|b)"))


