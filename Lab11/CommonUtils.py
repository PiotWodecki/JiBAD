import binascii
import hashlib
import os
from getpass import getpass

from JsonHandler import deserialize_users, deserialize_books
from User import User


def handle_user_input(n):
    while True:
        try:
            value = int(input())
        except ValueError:
            print("Wprowadź cyfrę odpowiadającą opcji.")
            continue

        if value <= 0 or value > n:
            print("Wprowadź cyfrę odpowiadającą opcji.")
            continue
        else:
            break

    return value


def handle_login():
    login = input("Login: ")
    if len(login) < 3:
        print("Login musi mieć więcej niż 3 znaki")
    if len(login) >= 10:
        print("Login musi mieć mniej niż 10 znaków")

    login = is_login_exists(login)

    return login


def is_correct_password(login):
    users = deserialize_users()
    pwd = input("Hasło: ") #tutaj powinno być getpass(), ale w pycharmie nie działa
    for user in users:
        if user['login'] == login:
            salt = user['passwordhashed'][:64]
            stored_password = user['passwordhashed'][64:]
            pwdhash = hashlib.pbkdf2_hmac('sha512',
                                          pwd.encode('utf-8'),
                                          salt.encode('ascii'),
                                          100000)
            pwdhash = binascii.hexlify(pwdhash).decode('ascii')
            break

    if pwdhash == stored_password:
        return True

    return False


def get_user(login):
    users = deserialize_users()
    for user in users:
        if user['login'] == login:
            return user


def is_login_exists(login):
    deserialized = deserialize_users()
    for d in deserialized:
        if d['login'] == login:
            return d['login']

    print("Brak użytkownika w systemie")


def user_input_book_properties():
    print("Dodawanie książki")
    title = input("Title: ")
    author = input("Author: ")
    if not validate_name_input(author):
        try:
            year = int(input("Year of publishment: "))
            if title is not None and author is not None and year > 1500 and year < 2021:
                return {'title' : title, 'author': author, 'year': year}

        except ValueError:
            print("Niepoprawne data")
    else:
        print("Informacje zostały dodane niepoprawnie")


def user_input_book_guid():
    clear_console()
    guid = input("GUID: ")
    if guid is not None:
        if if_book_exists(guid):
            return guid
    print("Brak książki, nie można usunąć")


def if_book_exists(guid):
    deserialized = deserialize_books()
    if guid is not None:
        for d in deserialized:
            if d['id'] == guid:
                return True

    return False


def create_user():
    login = input("Login: ")
    if len(login) <= 3 or len(login) >= 10:
        print("Nieprawidłowy login.")
    else:
        if is_user_exist(login):
                print("Login już istnieje")
        else:
            name = input("Name: ")
            surname = input("Surname: ")
            if validate_name_input(name) and validate_name_input(surname):
                password = input("Password: ")
                user = User(name, surname, login, password)
                return user
            else:
                print("Niepoprawne dane")


def is_user_exist(login):
    users = deserialize_users()
    for user in users:
        if user['login'] == login:
            return True

    return False


def book_to_borrow():
    title = input("Tytuł: ")
    author = input("Autor: ")
    book = is_book_exists(title, author)
    if book is not None:
        print("Pomyślnie wypożyczono książkę")
        return book['id']
    else:
        print("Nie można wypożyczyć ksiażki")


def is_book_exists(title, author):
    books = deserialize_books()
    for book in books:
        if book['title'] == title and book['author'] == author:
            if not book['loan']:
                return book


def validate_name_input(input_name):
    digits = any(char.isdigit() for char in input_name)
    correct_length = len(input_name) > 3 and len(input_name) < 15
    first_letter_upper = input_name.istitle()

    if not digits and correct_length and first_letter_upper:
        return True

    return False

def validate_author(input_author):
    digits = any(char.isdigit() for char in input_author)
    correct_length = len(input_author) > 3 and len(input_author) < 30

    if not digits and correct_length:
        return True

    return False

def clear_console(): #nie działa w pycharmie
    clear = lambda: os.system('cls')
    clear()


def cls(): #nie działa w pycharmie
    os.system('cls' if os.name=='nt' else 'clear')
