class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
    def area(self):
        return self.a * self.b / 2

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
ins = RightTriangle(input_c, input_a, input_b)

if (ins.c ** 2) == (ins.a ** 2) + (ins.b ** 2):
    print(ins.area())
else:
    print("Not right")


"""
class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2

    def area(self):
        return self.a * self.b / 2

    def verify(self):
        return self.c ** 2 == self.a ** 2 + self.b ** 2

# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)
if triangle.verify():
    print(triangle.area())
else:
    print("Not right")

"""
