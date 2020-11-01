from Employee import Employee
from Person import Person


class Educator(Employee, Person):

    def __init__(self, name, lastname, email, room_number, subjects, consultation):
        super().__init__(name, lastname, email, room_number)

        if subjects is None:
            self.subjects = []
        else:
            self.subjects = subjects

        if consultation is None:
            self.consultation = []
        else:
            self.consultation = consultation

    def __repr__(self):
        return 'Name:{} Lastname:{} Email:{} Inbox:{}, Room number:{}, Subjects:{}, Consulatations:{}'.format(self.name, self.lastname, self.email, self.inbox,
                                                                              self.room_number, self.subjects, self.consultation)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_consultation(self, consultation_time):
        self.consultation.append(consultation_time)


educator = Educator('Henryk', 'Malinowski', 'hmalinowiski@o2.pl', '320', ['Matematyka', 'Informatyka'], [('Poniedziaek', '14:00')])
print(educator)

