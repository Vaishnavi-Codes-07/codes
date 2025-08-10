class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning")


harry = Employee()
harry.language = "Java"  # This is a object/ instance attribute

harry.getInfo()
# Employee.getInfo(harry)

harry.greet()



