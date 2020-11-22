from Shape import Shape


class Circle(Shape):

    def __init__(self, name, size_radius):
        super().__init__(name)
        self.size_radius = size_radius
        self. rotation = 0

    def __repr__(self):
        return "Object: {}\nName: {}\nSize: {}\nCenter: {}\nRotation: {}\nBorder color: {}\n" \
               "Background color: {}".format(self.__class__.__name__, self.name, self.size_radius, self.center, self.rotation,
                                             self.border_color, self.background_color)




