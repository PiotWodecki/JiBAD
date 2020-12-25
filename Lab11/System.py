from Book import Book
from CommonUtils import handle_user_input, handle_login, user_input_book_properties, clear_console
import os

from JsonHandler import deserialize_users, deserialize_books


class System:

    def __init__(self):
        self.state = 'hello_screen'
        self.users = deserialize_users()
        self.books = deserialize_books()

    def run(self):
        while self.state != 'exit':

            if self.state == 'hello_screen':
                number_of_options = 4
                self.print_prompt()
                option = handle_user_input(number_of_options)
                self.handle_option(option)

            elif self.state == 'login':
                user = handle_login()
                if user is None:
                    self.state = 'hello_screen'
                else:
                    if user['is_employee']:
                        self.state = 'logged_employee'
                    else:
                        self.state = 'logged_client'

            elif self.state == 'logged_employee':
                clear_console()
                number_of_options = 4
                self.print_prompt()
                option = handle_user_input(number_of_options)
                self.handle_option(option)

            elif self.state == 'adding_book':
                book_input = user_input_book_properties()
                if book_input is not None:
                    book = self.create_book(book_input)
                    self.books.append(book)




    def print_prompt(self):
        clear_console()
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
            print('3. Usuń książkę do zbioru')
            print('4. Dodaj czytelnika')
        elif self.state == 'adding_book':
            print('Dodawanie książki')

    def handle_option(self, option):
        if self.state == 'hello_screen':
            if option == 4:
                self.state = 'exit'
                print('Dziękujemy i zapraszamy ponownie')
            elif option == 1:
                self.state = 'login'
            else:
                self.state = 'create_user'
        elif self.state == 'logged_employee':
            if option == 2:
                self.state = 'adding_book'
    @staticmethod
    def create_book(model):
        book = Book(model['title'], model['author'], model['year'])
        return book

