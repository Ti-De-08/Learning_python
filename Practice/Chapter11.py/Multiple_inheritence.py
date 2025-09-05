# This is a simple example of Multiple inheritance in Python

#class defined in the parent class
class Employee:
    company1 = "Google"
    name = "Defalut Name"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company1}")

#class defined in the child class
class Coder:
    company = "Microsoft"
    language = "Python"
    def printLanguage(self):
        print(f"The language of the coder is {self.language} and the company is {self.company}")

class Programmer (Employee, Coder): #Multiple inheritance
    company = "IBM" #class variable
    def primaryLanguage(self):
        print(f"The primary language of the coder is {self.language} and the company is {self.company}")         

a = Employee() #creating object of Employee class
b = Programmer() #creating object of Programmer class

b.show() #accessing instance method of Employee class
b.printLanguage() #accessing instance method of Coder class
b.primaryLanguage() #accessing instance method of Programmer class