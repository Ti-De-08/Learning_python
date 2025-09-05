#defining a class
class Programmer:
    company = "Microsoft" #class variable
    #defining the constructor
    def __init__(self, name, age, salary, id): #constructor with parameters

        self.name = name #instance variable
        self.age = age #instance variable
        self.salary = salary #instance variable
        self.id = id # instance variable

# creating objects/instances of the class

p1 = Programmer("Tirtha", 29, 100000, 2456) #instance 1/object 1
print(p1.name, p1.age, p1.salary, p1.id) #accessing instance/object variables

p2 = Programmer("Yash", 22, 120000, 2457) #object 2
print(p2.name, p2.age, p2.salary, p2.id) #accessing instance/object variables

p3 = Programmer("Sonu", 22, 120000, 2458) #object 3
print(p3.name, p3.age, p3.salary, p3.id) #accessing instance/object variables

    
