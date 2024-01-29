import math
import random


class S_add:

    def add_two_sring(self, s1, s2):
        return s1+" "+s2


class sum:
    def sum(self, x, y):
        return x+y


class GpaChecker:

    def check_gpa(self, gpa):
        if (gpa == 5.00):
            return "A+"
        elif (gpa >= 4.50 and gpa <= 4.99):
            return "A"
        elif (gpa >= 4.00 and gpa <= 4.49):
            return "B+"
        elif (gpa <= 3.99 and gpa >= 3.50):
            return "B-"
        elif (gpa <= 3.49 and gpa >= 3.00):
            return "C"


add = S_add()
print(add.add_two_sring("hi", "there"))
val = sum()
print(val.sum(1, 5))

gp = GpaChecker()
print(gp.check_gpa(5.00))

list = [1, 2, 3, 5, 32, 10]

print(random.choices(list, k=2))  # chese random two value
print(random.choice(list))
# chose a single value


def sun(a, b):
    return a+b


print(sun(7, 8))
