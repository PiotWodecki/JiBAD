import binascii #biblioteka do kodowania
import hashlib #biblioteka do hashowania
import os


class User:

    def __init__(self, name, surname, login, password, is_employee=False):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password
        self.is_employee = is_employee
        self.hash_password(password)


    def hash_password(self, password): #rozwiązanie pochodzi ze strony: https://www.vitoshacademy.com/hashing-passwords-in-python/
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        if password is not None and salt is not None:
            pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
            pwdhash = binascii.hexlify(pwdhash)

        self.passwordhashed = (salt + pwdhash).decode('ascii')

