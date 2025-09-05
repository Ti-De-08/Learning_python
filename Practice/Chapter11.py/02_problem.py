"""Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
‘Pets’. Add a method ‘bark’ to class ‘Dog’."""

class Animals:
    pass

class Pets:
    pass

class Dog:

    @staticmethod # define a static method 'bark' in class 'Dog'
    def bark(): # define a method 'bark' in class 'Dog'
        print("Bhow Bhow") # return a string "Woof! Woof!" when the method is called
    
a = Dog() # create an instance of class 'Dog'
a.bark() # call the method 'bark' on the instance 'a' and print the result
