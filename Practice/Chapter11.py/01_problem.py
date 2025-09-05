
"""Create a class (2-D vector) and use it to create another class representing a 3-D
vector."""

class Vector2D:

    
    def __init__(self, i, j):
        #initialize the 2-D vector with  i and j components
        self.i = i
        self.j = j
    
    def show(self): 
        #display the 2-D vector in the form of (i, j)
        print(f" The 2-D vector is {self.i}i + {self.j}j")

class Vector3D(Vector2D): #inheriting the 2-D vector class

    def __init__(self, i, j, k):
        super().__init__(i, j) #initialize the 3-D vector with i, j and k components
        self.k = k #class variable for 3-D vector

    def show(self):
        #display the 3-D vector in the form of (i, j, k)
        print(f" The 3-D vector is {self.i}i + {self.j}j + {self.k}k")

#creating an object of 2-D vector
v2 = Vector2D(1, 2)
v2.show() #calling the show method of 2-D vector

#creating an object of 3-D vector
v3 = Vector3D(4, 2, 3)
v3.show() #calling the show method of 3-D vector

