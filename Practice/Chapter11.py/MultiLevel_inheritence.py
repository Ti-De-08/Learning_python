class Employee:
    a = 1 #class variable


class Programmer(Employee):
    b = 2 #class variable

class Manager(Programmer):
    c = 3 #class variable

o = Employee() #creating object of Manager class
print(o.a) #accessing class variable of Employee class. Prints the 'a' attribute.
"""print(o.b) #accessing class variable of Programmer class. Prints error as 'b' attribute is not defined in Employee class."""

o = Programmer() #creating object of Manager class
print(o.a, o.b) #accessing class variable of Employee class and Programmer class. Prints the 'a' and 'b' attribute.
"""print(o.c) #accessing class variable of Programmer class. Prints the 'b' attribute."""

o = Manager() #creating object of Manager class
print(o.a, o.b, o.c) #accessing class variable of Employee class, Programmer class and Manager class. Prints the 'a', 'b' and 'c' attribute.
"""print(oaccessing class variable of Programmer class. Prints the 'b' attribute."""
