from Person import Person


class Employee(Person):

    def __init__(self, name, lastname, email, room_number):
        super().__init__(name, lastname, email)
        self.room_number = room_number

    def __repr__(self):
        return 'Name:{} Lastname:{} Email:{} Inbox:{}, Room number:{}'.format(self.name, self.lastname, self.email,
                                                                              self.inbox, self.room_number)

