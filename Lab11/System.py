from Book import Book
from CommonUtils import handle_user_input, handle_login, user_input_book_properties, clear_console, \
    user_input_book_guid, if_book_exists, create_user, cls, book_to_borrow, is_correct_password, get_user
import os

from JsonHandler import deserialize_users, deserialize_books, serialize_user_to_json, serialize_book_to_json


class System:

    def __init__(self):
        self.state = 'hello_screen'
        self.users = deserialize_users()
        self.books = deserialize_books()

    def run(self):
        while self.state != 'exit':

            if self.state == 'hello_screen':
                self.handle_welcome_screen()

            elif self.state == 'login':
                self.handle_login_screen()

            elif self.state == 'logged_employee':
                self.handle_logged_employee_screen()

            elif self.state == 'adding_book':
                self.handle_adding_book_screen()

            elif self.state == 'removing_book':
                self.handle_removing_book_screen()

            elif self.state == 'returning_book':
                self.handle_returning_book_screen()

            elif self.state == 'adding_user':
                self.handle_adding_user_screen()

            elif self.state == 'logged_client':
                self.handle_welcome_screen()

            elif self.state == 'search_book_set':
                self.handle_search_book_set_screen()

            elif self.state == 'borrow_book':
                self.handle_borrow_book_screen()

            elif self.state == 'add_employee_user':
                self.handle_add_user_screen(True)

            elif self.state == 'add_regular_user':
                self.handle_add_user_screen(False)

            else:
                self.state = 'hello_screen'

        serialize_user_to_json(self.users)
        serialize_book_to_json(self.books)

    def print_prompt(self):
        if self.state == 'hello_screen':
            print("Witamy w bibliotece! Co chcesz zrobić?\n")
            print("1. Zalogować się \n")
            print("2. Założyć konto użytkownika \n")
            print("3. Założyć konto pracownika \n")
            print("4. Wyjść \n")

        elif self.state == 'logged_employee':
            print('Konto pracownicze')
            print('Wybierz co chcesz zrobić: ')
            print('1. Przyjmij zwrot książki')
            print('2. Dodaj książkę do zbioru')
            print('3. Usuń książkę ze zbioru')
            print('4. Dodaj czytelnika')
            print('5. Wróć')
            print('6. Zamknij')

        elif self.state == 'adding_book':
            print('Dodawanie książki')

        elif self.state == 'adding_book':
            print('Usuwanie książki')

        elif self.state == 'returning_book':
            print("Przyjmowanie zwrotu książki")

        elif self.state == 'adding_user':
            print("Dodawnie użytkownika")

        elif self.state == 'logged_client':
            print('Konto użytkownika')
            print('Wybierz co chcesz zrobić: ')
            print("1. Przeszukaj katalog")
            print("2. Wypożycz książkę")
            print("3. Cofnij")
            print("4. Zamknij")

        elif self.state == 'borrow_book':
            print("Wypożycz książkę")

        elif self.state == 'search_book_set':
            print("Zbiór biblioteki")

        elif self.state == 'add_regular_user':
            print("Zakładanie konta użytkownika")

        elif self.state == 'add_employee_user':
            print("Zakładanie konta pracownika")

        else:
            self.state = 'hello_screen'

    def handle_option(self, option):
        if self.state == 'hello_screen':
            if option == 4:
                self.state = 'exit'
                print('Dziękujemy i zapraszamy ponownie')

            elif option == 1:
                self.state = 'login'

            elif option == 2:
                self.state = 'add_regular_user'

            elif option == 3:
                self.state = 'add_employee_user'

            else:
                self.state = 'hello_screen'

        elif self.state == 'logged_employee':
            if option == 2:
                self.state = 'adding_book'

            elif option == 3:
                self.state = 'removing_book'

            elif option == 1:
                self.state = 'returning_book'

            elif option == 4:
                self.state = 'adding_user'

            elif option == 5:
                self.state = 'hello_screen'

            else:
                self.state = 'exit'

        elif self.state == 'logged_client':
            if option == 1:
                self.state = 'search_book_set'

            elif option == 2:
                self.state = 'borrow_book'

            elif option == 3:
                self.state = 'hello_screen'

            else:
                self.state = 'exit'

        else:
            pass

    @staticmethod
    def create_book(model):
        book = Book(model['title'], model['author'], model['year'])
        return book

    def display_books(self):
        for index, book in enumerate(self.books):
            print(index + 1)
            print("Tytuł: {}".format(book['title']))
            print("Autor: {}".format(book['author']))
            print("Data wydania: {}".format(book['year_of_publishment']))
            if book['loan']:
                translate_bool = 'Tak'
            else:
                translate_bool = 'Nie'
            print("Czy wypożyczona: {}".format(translate_bool))
            print()
        self.exit_from_display()

    def exit_from_display(self):
        print("Naciśnij 1 by cofnąć")
        input = handle_user_input(1)
        if input == 1:
            self.state = 'logged_client'

    def create_account(self, is_employee=False):
        user = create_user()
        if user is not None:
            user.is_employee = is_employee
            self.users.append(user)
            serialize_user_to_json(self.users)
            print("Pomyślnie dodano użytkownika")
        else:
            print("Nie udało się dodać użytkownika")
        self.state = 'hello_screen'

    def handle_welcome_screen(self):
        number_of_options = 4
        self.print_prompt()
        option = handle_user_input(number_of_options)
        self.handle_option(option)

    def handle_login_screen(self):
        login = handle_login()

        if login is None:
            pass

        else:
            if not is_correct_password(login):
                print("Niepoprawne hasło")
            else:
                user = get_user(login)
                if user is None:
                    self.state = 'hello_screen'
                else:
                    if user['is_employee']:
                        self.state = 'logged_employee'
                    else:
                        self.state = 'logged_client'

    def handle_logged_employee_screen(self):
        number_of_options = 6
        self.print_prompt()
        option = handle_user_input(number_of_options)
        self.handle_option(option)

    def handle_adding_book_screen(self):
        book_input = user_input_book_properties()
        if book_input is not None:
            book = self.create_book(book_input)
            self.books.append(book)
            serialize_book_to_json(self.books)
            print("Pomyślnie dodano")
            self.state = 'logged_employee'

    def handle_removing_book_screen(self):
        guid = user_input_book_guid()
        for book in self.books:
            if book['id'] == guid:
                self.books.remove(book)
                serialize_book_to_json(self.books)
                print("Pomyślnie usunięto")
                break

        serialize_book_to_json(self.books)
        self.state = 'logged_employee'

    def handle_returning_book_screen(self):
        guid = user_input_book_guid()
        for d in self.books:
            if d['id'] == guid:
                if d['loan']:
                    d['loan'] = False
                    serialize_book_to_json(self.books)
                    print("Zmieniono status")
                    break
                else:
                    print("Książka jest niewypożyczona")
                    break
        self.state = 'logged_employee'

    def handle_adding_user_screen(self):
        user = create_user()
        if user is not None:
            self.users.append(user)
            serialize_user_to_json(self.users)
            print("Pomyślnie dodano użytkownika")
        else:
            print("Nie udało się dodać użytkownika")
        self.state = 'logged_employee'

    def handle_search_book_set_screen(self):
        self.display_books()
        self.state = 'logged_client'

    def handle_borrow_book_screen(self):
        book_id = book_to_borrow()
        if book_id is not None:
            for book in self.books:
                if book['id'] == book_id:
                    book['loan'] = True
                    serialize_book_to_json(self.books)
        self.state = 'logged_client'

    def handle_add_user_screen(self, is_employee):
        self.create_account(is_employee)
        serialize_user_to_json(self.users)
        self.state = 'hello_screen'