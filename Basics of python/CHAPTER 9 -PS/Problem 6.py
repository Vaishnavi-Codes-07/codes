# WAP TO MINE A LOG FILE AND FIND OUT WHETHER IT CONTAINS PYTHON.

with open("log.txt") as f:
    content = f.read()

if("python" in content):
    print("yes python is present")
else:
    print("python is not present")