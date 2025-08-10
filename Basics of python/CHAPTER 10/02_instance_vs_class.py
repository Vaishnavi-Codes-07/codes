class Employee:
    language = "Py"  # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"  # This is a object/ instance attribute
print(harry.name, harry.salary, harry.language)

Vaishnavi = Employee()
Vaishnavi.name = "Vaishnavi"
print(Vaishnavi.name, Vaishnavi.salary, Vaishnavi.language)

# here is name is object attribute and salary and language are 
# class attribute they directly belongs to the class 