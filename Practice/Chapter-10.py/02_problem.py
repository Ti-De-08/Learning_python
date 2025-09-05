"""Write a class “Calculator” capable of finding square, cube and square root of a number.
Add a static method to greet the user with hello."""


#defining a class named Calculator
class Calculator:
   
   ##defining the constructor
    def __init__(self, n):
        self.n = n

    #defining a method to calculate the square of the number
    def square(self):
        print(f"The square of the number is {self.n ** 2}")

    def cube(self):
        print(f"The cube of the number is {self.n ** 3}")

    def sqrt(self):
        print(f"The square root of the number is {self.n ** (1/2)}")

    @staticmethod #Not using self because I don't need to access any instance attributes.

    def greet():
        print("Hello! Welcome to the calculator program.")

a = Calculator(4) #creating an object of the class
a.greet() #calling the static method of the class
a.square() #calling the method of the class
a.cube() #calling the method of the class
a.sqrt() #calling the method of the classc  