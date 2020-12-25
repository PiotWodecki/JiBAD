from json import JSONEncoder


class EncodeUser(JSONEncoder):
    def default(self, o):
        return o.__dict__
