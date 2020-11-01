class Person:

    def __init__(self, name, lastname, email):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.inbox = []

    def __repr__(self):
        return '{} {} {} {}'.format(self.name, self.lastname, self.email, self.inbox)

    def send_email(self, sender, message):
        self.inbox.append((sender, message))




