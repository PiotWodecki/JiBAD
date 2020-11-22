import os
import re
import string

from Circle import Circle
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from Vector import Vector

starting_sentence = """
This program allows you to make basic operation on shapes. Please follow the instruction.
Instructions:
add <figure> <name> <size>
remove <name>
move <name> <vector>
scale <name> <ratio>
rotate <name> <angle>
set border color <name> <color>
set background color <name> <color>
help
quit

Let's start
        """


class CommandHandler:

    def __init__(self):
        self.shapes_dict = {}

    def run(self):
        print(starting_sentence)

        try:
            CommandHandler.handle_input(self)
            # print(repr(self.shapes_dict))
            print(CommandHandler.print_dictionary(self))
            CommandHandler.write_shapes_to_dictionary(CommandHandler.print_dictionary(self))
        except ValueError:
            print("Try again")
        except IOError:
            print("File does not exist")

    def handle_input(self):
        commands = ["help", "quit", "add", "remove", "move", "scale", "rotate", "set"]
        while True:
            try:
                command = input().lower()
                if command.split(None, 1)[0] in commands:
                    if command == "help":
                        CommandHandler.handle_help_command()
                    elif command == "quit":
                        break
                    else:
                        CommandHandler.handle_parameters(self, command)
                else:
                    raise ValueError
            except ValueError:
                print("Command is incorrect")

    def handle_parameters(self, command):
        instruction = command.split(None, 1)[0]
        if instruction == "add":
            CommandHandler.handle_add_command(self, command)
        elif instruction == "remove":
            CommandHandler.handle_remove_command(self, command)
        elif instruction == "move":
            CommandHandler.handle_move_command(self, command)
        elif instruction == "scale":
            CommandHandler.handle_scale_command(self, command)
        elif instruction == "rotate":
            CommandHandler.handle_rotate_command(self, command)
        elif instruction == "set":
            if ' '.join(command.split()[:3]) == "set border color" or ' '.join(command.split()[:3]) == "set background color":
                CommandHandler.handle_setting_border_color(self, command)
        else:
            raise ValueError

    def handle_setting_border_color(self, command):
        try:
            CommandHandler.handle_colors(self, command)
        except IndexError:
            print("Incorrect number of arguments")
        except ValueError:
            print("Arguments not proper")
        except KeyError:
            print("Shape with this key does not exist")

    def handle_colors(self, command):
        command = command.split()
        color = command[4]
        colors = ['black', 'white', 'red', 'green', 'blue', 'cyan', 'magenta', 'yellow']

        if len(command) != 5:
            raise IndexError

        if command[3] not in self.shapes_dict.keys():
            raise KeyError

        if color in colors:
            shape = self.shapes_dict[command[3]]
            if command[1] == "background":
                shape.background_color = color
            else:
                shape.border_color = color
        else:
            raise ValueError

    def handle_rotate_command(self, command):
        try:
            CommandHandler.handle_rotate(self, command)
        except IndexError:
            print("Incorrect number of arguments")
        except ValueError:
            print("Arguments not proper")
        except KeyError:
            print("Shape with this key does not exist")

    def handle_rotate(self, command):
        command = command.split()
        rotation = command[2]

        if len(command) != 3:
            raise IndexError

        if command[1] not in self.shapes_dict.keys():
            raise KeyError

        if float(rotation) > 0:
            shape = self.shapes_dict[command[1]]
            if type(shape) is Circle:
                raise ValueError
            else:
                shape.rotation = float(shape.rotation) + float(rotation)
        else:
            raise ValueError

    def handle_scale_command(self, command):
        try:
            CommandHandler.handle_scale(self, command)
        except IndexError:
            print("Incorrect number of arguments")
        except ValueError:
            print("Arguments not proper")
        except KeyError:
            print("Shape with this key does not exist")

    def handle_scale(self, command):
        command = command.split()
        size = command[2]

        if len(command) != 3:
            raise IndexError

        if command[1] not in self.shapes_dict.keys():
            raise KeyError

        if float(size) > 0:
            shape = self.shapes_dict[command[1]]
            if type(shape) is Circle:
                shape.size_radius = float(shape.size_radius) * float(size)
            elif type(shape) is Square:
                shape.size_a = float(shape.size_a) * float(size)
            elif type(shape) is Rectangle:
                shape.size_a = float(shape.size_a) * float(size)
                shape.size_b = float(shape.size_b) * float(size)
            else:
                shape.size_a = float(shape.size_a) * float(size)
                shape.size_b = float(shape.size_b) * float(size)
                shape.size_c = float(shape.size_c) * float(size)
        else:
            raise ValueError

    def handle_add_command(self, command):
        try:
            self.handle_add(command)
        except ValueError:
            print("Arguments not proper")

        except KeyError:
            print("Shape with this key already exist")

        except IndexError:
            print("Incorrect number of arguments")

    def handle_add(self, command):
        command = command.split()
        figures = ["circle", "square", "rectangle", "triangle"]

        if command[1] not in figures:
            raise ValueError

        if command[2] in self.shapes_dict.keys():
            raise KeyError

        if command[2] not in set(string.ascii_lowercase + string.digits + '_') and command[2][0].isdigit():
            raise ValueError

        if float(command[3]) <= 0:
            raise ValueError

        if command[1] == "square":
            if (len(command) == 5 and command[3] == command[4]) or len(command) == 4:
                CommandHandler.add(self, command)
            else:
                raise IndexError
        elif command[1] == "circle":
            if len(command) == 4:
                CommandHandler.add(self, command)
            else:
                raise IndexError
        elif command[1] == "rectangle":
            if len(command) == 5:
                CommandHandler.add(self, command)
            else:
                raise IndexError
        else:
            if len(command) == 6:
                if CommandHandler.check_triangle_validity(command[3], command[4], command[5]):
                    CommandHandler.add(self, command)
                else:
                    raise ValueError
            else:
                raise IndexError

    def handle_remove_command(self, command):
        try:
            CommandHandler.handle_remove(self, command)

        except ValueError:
            print("Argument not proper")

        except KeyError:
            print("Shape with this name does not exist")

    def handle_remove(self, command):
        command = command.split()

        if len(command) != 2:
            raise ValueError

        if command[1] in self.shapes_dict.keys():
            del self.shapes_dict[command[1]]
        else:
            raise KeyError

    def handle_move_command(self, command):
        try:
            CommandHandler.handle_move(self, command)

        except ValueError:
            print("Argument is not correct")

        except KeyError:
            print("Name does not exist")

    def handle_move(self, command):
        command = command.split()
        pattern_vector = re.compile("^\([ ]*[-]{,1}[ ]*[0-9]+[ ]*[,][ ]*[-]{,1}[ ]*[0-9]+[ ]*\)$")

        if command[1] not in self.shapes_dict.keys():
            raise KeyError

        if re.match(pattern_vector, command[2]):
            shape = self.shapes_dict[command[1]]
            vector_x = float(re.search('\((.*),', command[2]).group(1))
            vector_y = float(re.search(',(.*)\)', command[2]).group(1))
            shape.center = shape.center + Vector(vector_x, vector_y)
        else:
            raise ValueError

    def add(self, parameters):
        if parameters[1] == "circle":
            self.shapes_dict[parameters[2]] = Circle(parameters[2], parameters[3])
        elif parameters[1] == "square":
            self.shapes_dict[parameters[2]] = Square(parameters[2], parameters[3])
        elif parameters[1] == "rectangle":
            self.shapes_dict[parameters[2]] = Rectangle(parameters[2], parameters[3], parameters[4])
        else:
            self.shapes_dict[parameters[2]] = Triangle(parameters[2], parameters[3], parameters[4], parameters[5])

    @staticmethod
    def write_shapes_to_dictionary(text):
            shapes_txt = os.path.join(os.getcwd(), 'shapes.txt')
            if os.path.exists(shapes_txt):
                with open('shapes.txt', 'w') as f:
                    print(text, file=f)
            else:
                raise IOError

    def print_dictionary(self):
        output = ""
        for k in self.shapes_dict:
            output += k
            output += "\n"
            output += self.shapes_dict[k].__repr__()
            output += "\n\n"

        return output

    @staticmethod
    def check_triangle_validity(a, b, c):
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            return False
        else:
            return True

    @staticmethod
    def handle_help_command():
        help_sentence = """
This program allows you to make basic operations on shapes. Please follow the instruction.
Instructions:
add <figure> <name> <size>
remove <name>
move <name> <vector>
scale <name> <ratio>
rotate <name> <angle> - does not involve circle
set border color <name> <color>
set background color <name> <color>
help
quit

<figure> - one of: circle, square, rectangle, triangle
<name> - unique id which can contain letters, numbers, underlines. It can't start from number
<ratio> - any real number, number =/= 0
<angle> - any angle in degree
<color> - one of: black, white, red, green, blue, cyan, magenta, yellow
        """
        print(help_sentence)




