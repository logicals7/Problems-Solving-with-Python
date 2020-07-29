class Student:
    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = self.name[0] + last_name + birth_year

# Getting input
inp_name = input()
inp_last_name = input()
inp_birth_year = input()

# Creating Instance
s = Student(inp_name, inp_last_name, inp_birth_year)

# Printing Id
print(s.id)
