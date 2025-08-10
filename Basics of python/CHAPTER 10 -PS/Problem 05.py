# Write a class Train which has methods to book a ticket, get status(no of seats) and get fare information of train running user Indian Railways.
# import random or

from random import randint

class Train: 
    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} Is Running on time" )

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint (222, 5555)}")

t = Train(12399)

t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")


# from random import randint

# class Train: 
#     def __init__(self, trainNo):
#         self.trainNo = trainNo

#     def book(self, fro, to):
#         print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

#     def getStatus(self):
#         print(f"Train no: {self.trainNo} is running on time")

#     def getFare(self, fro, to):
#         fare = randint(222, 5555)
#         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is ₹{fare}")

# # Creating an instance of the Train class
# t = Train(12399)

# # Calling the methods
# t.book("Rampur", "Delhi")
# t.getStatus()
# t.getFare("Rampur", "Delhi")
