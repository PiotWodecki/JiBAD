from Shape import Shape


class Square(Shape):

    def __init__(self, name, size_a):
        super().__init__(name)
        self.size_a = size_a

    def __repr__(self):
        return "Object: {}\nName: {}\nSize: {}\nCenter: {}\nRotation: {}\nBorder color: {}\n" \
               "Background color: {}".format(self.__class__.__name__, self.name, self.size_a, self.center, self.rotation % 360,
                                             self.border_color, self.background_color)
