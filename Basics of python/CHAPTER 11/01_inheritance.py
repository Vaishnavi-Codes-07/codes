class Employee:
    company = "ITC"        # class variable
    def __init__(self):
        pass
    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")

class Programmer(Employee): # arguement
    company = "ITC Infotech" # class variable 

    def __init__(self, name, salary): 
       self.name = name     # instance variables 
       self.salary = salary

    def show(self):
        print(f"The name of the employee is {self.name} and salary is {self.salary}")
        

omkar = Employee("omkar", 9898)

