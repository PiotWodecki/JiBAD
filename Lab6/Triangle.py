from Shape import Shape


class Triangle(Shape):

    def __init__(self, name, size_a, size_b, size_c):
        super().__init__(name)
        self.size_a = size_a
        self.size_b = size_b
        self.size_c = size_c

    def __repr__(self):
        return "Object: {}\nName: {}\nSize a: {}\nSize_b: {}\nSize_c: {}\nCenter: {}\nRotation: {}\nBorder color: {}\n" \
               "Background color: {}".format(self.__class__.__name__, self.name, self.size_a, self.size_b,self.size_c,
                                             self.center, self.rotation,
                                             self.border_color, self.background_color)
