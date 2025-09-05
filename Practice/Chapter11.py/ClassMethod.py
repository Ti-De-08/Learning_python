class Employee:
    a = 1 #class variable

    def show(self):
        print(f"The class attribute of a is {self.a}")

e = Employee() #creating object of Employee class
e.a = 22 #creating instance variable of Employee class
e.show() #accessing instance method of Employee class
print(e.a) #accessing instance variable of Employee class

print("The program prints both the class variable and instance variable of the Employee class as 22")
print(" ")

'''Now if we want to access the class variable of the Employee class,
 we can do it by using the decorator @classmethod.'''

class Employee:
    a = 1 #class variable aka class attribute

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee() #creating object of Employee class
e.a = 22 #creating instance variable of Employee class
e.show() #accessing instance method of Employee class
print("As the class method is used, the class variable of Employee class is printed as 1")

"""Class attirbute is a variable that is shared by all instances of a class and
instance attribute is a variable that is unique to each instance of a class."""