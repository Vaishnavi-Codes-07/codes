st = "Hey Harry you are amazing"

f = open("file.txt" , "w")

data = f.write(st)
print(data)
f.close()