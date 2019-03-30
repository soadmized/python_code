class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, 'is', self.age, 'years old')

john = Person('John', 21)

lucy = Person('Lucy', 21)

Person.print_info(john)
lucy.print_info()
