class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Name {self.first_name} last_name{self.last_name}, age: {self.age}, gender: {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super(Student, self).__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return (f'Name {self.first_name} last_name{self.last_name}, '
                f'age: {self.age}, gender: {self.gender}, record_book: {self.record_book}')

    def __eq__(self, other):
        return str(self) == str(other)

    def __hash__(self):
        return hash(str(self))

