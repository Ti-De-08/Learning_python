"""Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
and get fare information of train running under Indian Railways."""

from random import randint #importing randint from random module to generate random numbers
from random import randrange #importing randrange from random module to generate random numbers
#defining a class named Train
class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    
    def book(self, From, to):
        print(f"Ticket is booked from {From} to {to} in train {self.trainNo}.")

    def getStastus(self):
        print(f"Total number of seats left in train {self.trainNo} is {randint(0,1200)}.")

    def getFare(self, From, to):
        print(f"Fare from {From} to {to} in train {self.trainNo} is {randrange(100, 2000, 25) } rupees.")  


trainNo = randint(10000, 99999) #generating a random number between 10000 and 99999

#creating an object of the class
t = Train(trainNo)
t.book("Delhi", "Mumbai") #calling the method of the class
t.getStastus() #calling the method of the class
t.getFare("Delhi", "Mumbai") #calling the method of the class