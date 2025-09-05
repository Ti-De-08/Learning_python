class Example:
    class_variable = "Python"

    @staticmethod
    def static_method():
        return "This is a static method"
  

    @classmethod
    def class_method(cls):
        return f"This is a class method accessing: {cls.class_variable}"
    
    
# Calling methods
print(Example.static_method())   # ✅ Works without needing an instance
print("No need for self or cls in static method")
print(Example.class_method())    # ✅ Works and accesses class variables
print("Need cls in class method")

"""
Feature                          |@staticmethod      | @classmethod
Needs self?                      | ❌ No            | ❌ No
Needs cls?                       | ❌ No            | ✅ Yes
Can access instance attributes?  | ❌ No            | ❌ No
Can access class attributes?     | ❌ No            | ✅ Yes
"""

"""
✅ Use @staticmethod for pure functions that don't touch instance/class data.
✅ Use @staticmethod if the function is logically related to the class but doesn't need instance or class data.

✅ Use @classmethod if you need to modify/access class attributes.


✅ Avoid @staticmethod if the function should be independent—put it outside the class instead.
✅ Avoid @classmethod if you don't need to access or modify class attributes.
"""