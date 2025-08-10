
'''
for n = 3
   *
  ***
 ***** 

 '''

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(" "* (n-i), end="")    #(, end="") dont give new line by defult
    print("*"* (2*i-1), end="")
    print("")



