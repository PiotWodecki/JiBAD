from Person import Person


class Student(Person):

    def __init__(self, name, lastname, email, index_number):
        super().__init__(name, lastname, email)
        self.index_number = index_number
        self.all_grades = dict()
        self.grades_from_subject = dict()
        self.key = 1

    def __repr__(self):
        return 'Name:{} Lastname:{} Email:{} Inbox:{}, All grades:{} Grades from subjects{}'\
            .format(self.name, self.lastname, self.email, self.inbox, self.all_grades, self.grades_from_subject)

    def add_grade(self, grade):
        self.all_grades[self.key] = grade
        self.key += 1

    def add_grade_from_subject(self, grade, subject):
        self.grades_from_subject[subject] = grade


student = Student('Juliusz', 'Cezar', 'jcezar@gmail.com', '22222')
print(student)
student.add_grade(5)
student.add_grade(4)
student.add_grade(3)
student.add_grade_from_subject(5, 'JiBAD')
student.send_email('Pan Paweł', 'Ała')
student.send_email('Pan Paweł2', 'Ała2')
print(student)