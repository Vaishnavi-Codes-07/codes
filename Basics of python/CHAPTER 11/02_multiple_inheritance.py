class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the company is {self.company}" )

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all languages here is your language: {self.language} language")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and the company is {self.company}" )
 
a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()

