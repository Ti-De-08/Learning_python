# Base Class  
class Employee:

    company = "IBM" #class variable
    name = "Tirtha" #class variable
    language = "Python" #class variable
    
    #Function to initialize the object of the class
    def show(self): #instance method
        print(f"The name of the employee is {self.name} and the company is {self.company}")

#child class of Employee class
class Programmer(Employee): 
    company = "Google" #class variable
  
   
    def printLanguage(self): #instance method
        print(f"The language of the coder-{self.name} is {self.language} and the company is {self.company}")


a = Employee() #creating object of Employee class

b = Programmer() #creating object of Programmer class

print(a.company, b.company) #accessing class variable of Employee class and Programmer class


#b.show() #accessing instance method of Employee class
#b.printLanguage() #accessing instance method of Employee class   

""" Here we have created a class Employee and a child class Programmer. 
 The child class Programmer inherits the properties of the parent class Employee.
 The child class can access the properties of the parent class.
 The child class can also override the properties of the parent class."""