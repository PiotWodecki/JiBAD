from Vector import Vector


class Shape:

    def __init__(self, name):
        self.name = name
        self.center = Vector(0, 0)
        self.rotation = 0
        self.background_color = None
        self.border_color = None

    def __repr__(self):
        return "Object: {}\nName: {}\nCenter: {}\nRotation: {}\nBorder color: {}\n" \
               "Background color: {}".format(self.__class__.__name__, self.name, self.center, self.rotation % 360,
                                             self.border_color, self.background_color)
