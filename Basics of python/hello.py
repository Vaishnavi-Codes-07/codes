class Person :
    def __init__(self, name):
        self.name = name
    def printName(self):
        print("Hello "+ self.name)


p1 = Person("omkar")
p1.printName()