
class Employee:
    def __init__(self) -> None:
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is not b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = manager()
print(o.a, o.b, o.c)

class Employee:
    def __init__(self) -> None:
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    b = 2

class manager(Programmer):
    c = 3

o = Employee()
print(o.a) # Prints the a attribute
# print(o.b) # Shows an error as there is not b attribute in Employee class

o = Programmer()
print(o.a, o.b)


o = manager()
print(o.a, o.b, o.c)

