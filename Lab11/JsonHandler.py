import json

from Book import Book
from User import User


def serialize_user_to_json(user):
    with open('users.json', 'w') as f:  # writing JSON object
        json.dump(user, f, indent=2, default=encoder_user)


def serialize_book_to_json(book):
    with open('books.json', 'w') as f:  # writing JSON object
        json.dump(book, f, indent=2, default=encoder_book)


def deserialize_users():
    with open("users.json", 'r') as f:
        data = json.load(f)

    deserialized_objects = []

    if isinstance(data, dict):
        pass
    else:
        # In this case you are getting list of dictionaries so you
        # may get multiple id's.
        # Response shared by you has only one dictionary in list.
        for d in data:  # Iterate over all dict in list
            deserialized_objects.append(d)

        return deserialized_objects

    return data


def deserialize_books():
    with open("books.json", 'r') as f:
        data = json.load(f)

    deserialized_objects = []

    if isinstance(data, dict):
        pass
    else:
        # In this case you are getting list of dictionaries so you
        # may get multiple id's.
        # Response shared by you has only one dictionary in list.
        for d in data:  # Iterate over all dict in list
            deserialized_objects.append(d)

        return deserialized_objects

    return data


def encoder_user(user):
    if isinstance(user, User):
        return {'name': user.name, 'surname': user.surname, 'login': user.login, 'password': user.password, 'is_employee': user.is_employee}

    raise TypeError(f'Object {user} is not type of User')

def encoder_book(book):
    if isinstance(book, Book):
        return {'id': book.id, 'title': book.title, 'author': book.author, 'year_of_publishment': book.year_of_publishment, 'loan': book.loan}

    raise TypeError(f'Object {book} is not type of Book')


# user1 = User("Piotr6", "Woda", "wdck", "admin")
# user2 = User("Piotr2", "Woda", "wdck2", "admin")
# user3 = User("Piotr3", "Woda3", "wdck3", "admin", True)
# users = [user1, user2, user3]
# serialize_user_to_json(users)

# book1 = Book("Ogniem i mieczem", "Pan pawel", 1200)
# book2 = Book("Ogniem i mieczem2", "Pan pawel2", 1300)
# books = [book1, book2]
# serialize_book_to_json(books)

# deserialized = deserialize_users()
# print(deserialized)
# print(type(deserialized))
# for d in deserialized:
#     print(d['name'])

