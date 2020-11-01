from Employee import Employee
from Person import Person


class Researcher(Employee, Person):

    def __init__(self, name, lastname, email, room_number, publication):
        super().__init__(name, lastname, email, room_number)
        if publication is None:
            self.publication = []
        else:
            self.publication = publication

    def __repr__(self):
        return 'Name:{} Lastname:{} Email:{} Inbox:{}, Room number:{}, Publications:{}'.format(self.name, self.lastname, self.email, self.inbox,
                                                                              self.room_number, self.publication)

    def add_publication(self, title):
        self.publication.append(title)


researcher = Researcher('Jan', 'Nowak', 'jannowak@gmail.com', '420', ['Python', 'c#'])
researcher.send_email('Dawid Podsiadło', 'Nie ma fal')
print(researcher)