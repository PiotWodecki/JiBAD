from Shape import Shape


class Rectangle(Shape):

    def __init__(self, name, size_a, size_b):
        super().__init__(name)
        self.size_a = size_a
        self.size_b = size_b

    def __repr__(self):
        return "Object: {}\nName: {}\nSize a: {}\nSize_b: {}\nCenter: {}\nRotation: {}\nBorder color: {}\n" \
               "Background color: {}".format(self.__class__.__name__, self.name, self.size_a, self.size_b, self.center, self.rotation % 360,
                                             self.border_color, self.background_color)