from json import JSONEncoder


class EncodeUser(JSONEncoder):  # brzmi jak nazwa metody
    def default(self, o):
        return o.__dict__
