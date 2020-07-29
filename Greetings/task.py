class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print(f'Hello, I am {self.name}!')

inp_name = input()
s = Person(inp_name)
# s.greet()
Person.greet(s)