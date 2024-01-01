# Student(College, year, degree) IS A Person(name, address)

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __repr__(self):
        return repr((self.name, self.address))


class Student(Person):
    def __init__(self, name, college_name, address, year):
        super().__init__(name, address)
        self.college_name = college_name
        self.address = address
        self.year = year

    def __repr__(self):
        return repr((self.name, self.college_name, self.address, self.year))


person = Person("The Guy", "The address")
student = Student("Some Guy", "Some Engineering College", "Some address", "2023")

print(person)
print(student)
