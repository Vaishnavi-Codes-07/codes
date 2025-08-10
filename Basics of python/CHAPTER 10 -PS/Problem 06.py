#Can you change the self parameter inside a class to something else (say "harry"). try changing self to "slf" or "harry" and see the effects.


from random import randint

class Train: 
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(slf, fro, to):
        print(f"Ticket is booked in train no: {slf.trainNo} from {fro} to {to}")

    def getStatus(slf):
        print(f"Train no: {slf.trainNo} Is Running on time" )

    def getFare(slf, fro, to):
        print(f"Ticket fare in train no: {slf.trainNo} from {fro} to {to} is {randint (222, 5555)}")

t = Train(12399)

t.book("Rampur", "Delhi")
t.getStatus()
t.getFare("Rampur", "Delhi")
