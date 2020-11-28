class CommonUtils:

    @staticmethod
    def get_three_numbers():
        try:
            a = input("a = ")
            b = input("b = ")
            c = input("c = ")

            if CommonUtils.is_float(a) and CommonUtils.is_float(b) and CommonUtils.is_float(c):
                return [float(a), float(b), float(c)]
            else:
                raise ValueError

        except ValueError:
            return "Input is incorrect"

    @staticmethod
    def get_two_points():
        try:
            x1 = input("x1 = ")
            y1 = input("y1 = ")
            x2 = input("x2 = ")
            y2 = input("y2 = ")

            if CommonUtils.is_float(x1) and CommonUtils.is_float(y1) \
                    and CommonUtils.is_float(x2) and CommonUtils.is_float(y2):
                return [float(x1), float(y1), float(x2), float(y2)]
            else:
                raise ValueError

        except ValueError:
            return "Input is incorrect"

    @staticmethod
    def is_float(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

