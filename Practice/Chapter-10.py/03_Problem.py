"""Create a class with a class attribute a; create an object from it and set ‘a’
directly using ‘object.a = 0’. Does this change the class attribute?"""

# defining a class 

class Demo:

    a = 5 # class attribute

object = Demo() # creating an object of the class
print(object.a) # accessing the class attribute using the object
"""prints the class attribute because instance attribute is not is not present"""

object.a = 0 # setting a instance attribute using the object
print(object.a) # accessing the instance attribute using the object
"""prints the instance attribute because instance attribute is present and it is not same as class attribute"""

print(Demo.a) # accessing the class attribute using the class name
"""prints the class attribute because instance attribute is not is not present"""
