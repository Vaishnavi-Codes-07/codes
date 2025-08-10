marks = {
    "Harry": 100,
    "Omkar": 56,
    "Ajay": 23
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Harry"))
print(marks["Harry"])

print(marks.get("Harry2"))  # prints none
print(marks["Harry2"])  # returns an error
