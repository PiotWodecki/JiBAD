import json

from Book import Book
from User import User


def serialize_user_to_json(user):
    with open('users.json', 'w') as f:
        json.dump(user, f, indent=2, default=encoder_user)


def serialize_book_to_json(book):
    with open('books.json', 'w') as f:
        json.dump(book, f, indent=2, default=encoder_book)


def deserialize_users():
    with open("users.json", 'r') as f:
        data = json.load(f)

    deserialized_objects = []

    if isinstance(data, dict):
        pass
    else:
        for d in data:
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
        for d in data:
            deserialized_objects.append(d)

        return deserialized_objects

    return data


def encoder_user(user): #encoding pochodzi z poradnika
    if isinstance(user, User):
        return {'name': user.name, 'surname': user.surname, 'login': user.login,
                'is_employee': user.is_employee, 'passwordhashed': user.passwordhashed}

    raise TypeError('Object {} is not type of User'.format(user))


def encoder_book(book): #encoding pochodzi z poradnika
    if isinstance(book, Book):
        return {'id': book.id, 'title': book.title, 'author': book.author, 'year_of_publishment': book.year_of_publishment, 'loan': book.loan}

    raise TypeError(f'Object {book} is not type of Book')

#ręczne generowanie userów
user1 = User("Alfred", "Kokos", "kokos", "admin")
user2 = User("Witold", "Gombrowicz", "geba", "admin")
user3 = User("Pan", "Pracownik", "admin", "admin", True)
user3 = User("Pani", "Pracowniczka", "adminka", "admin", True)
users = [user1, user2, user3]
#serialize_user_to_json(users)

#ręczne generowanie książek
book1 = Book("Ogniem i mieczem", "Pan pawel", 1900)
book2 = Book("Ogniem i mieczem2", "Henryk Sienkiewicz", 1932)
book3 = Book("Mieczem i szablą", "Senryk Hienkiewicz", 2007)
book4 = Book("Piescia i noga", "Pan autor", 1821)
book5 = Book("Piescia i noga", "Pan autor", 1829)
book6 = Book("Piescia i noga", "Pan autor", 1826)
books = [book1, book2, book3, book4, book5, book6]
#serialize_book_to_json(books)


