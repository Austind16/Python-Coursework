from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Train ticket is booked from {fro} to {to}")
    def getStatus(self):
        print(f"Train no. {self.trainNo} is running on time")
    def getFare(self, fro, to):
        print(f"Train ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}") 

t = Train(12099)
t.book("Bharuch", "Ahmedabad")
t.getStatus()
t.getFare("Bharuch", "Ahmedabad")