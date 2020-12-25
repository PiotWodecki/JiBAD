import os

from JsonHandler import deserialize_users


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
    print("Login: ")
    login = input()
    if len(login) < 3:
        print("Login musi mieć więcej niż 3 znaki")
    else:
        user = is_login_exists(login)

    return user


def is_login_exists(login):
    deserialized = deserialize_users()
    for d in deserialized:
        if d['login'] == login:
            return d

    print("Brak użytkownika w systemie")
    return None


def user_input_book_properties():
    clear_console()
    title = input("Title: ")
    author = input("Author: ")
    year = int(input("Year of publishment: "))

    if title is not None and author is not None and year > 1500:
        return {'title' : title, 'author': author, 'year': year}
    else:
        print("Informacje zostały dodane niepoprawnie")

def clear_console():
    clear = lambda: os.system('cls')
    clear()