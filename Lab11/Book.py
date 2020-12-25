import random
from uuid import uuid4


class Book:

    def __init__(self, title, author, year_of_publishment):
        self.id = str(uuid4())
        self.title = title
        self.author = author
        self.year_of_publishment = year_of_publishment
        self.loan = False


def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1
