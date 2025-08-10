#(if elif and else) are comparision\relational operators 

# a = int(input("Enter you age: "))

# if else statement
# if(a>=18):
#     print("You are above age consent")
#     print("Good for you")

# else:
#     print("You are below the age of consent")

# print("End of program")

a = int(input("Enter you age: "))

#If elif else ladder

if(a>=18):
    print("You are above age consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")

else:
    print("You are below the age of consent")

print("End of program")

