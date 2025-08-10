# 6 is a perfect number 
# Divisors of 6 = 1 2 3 = 1 + 2 + 3 = 6

num = int(input("Enter a number: "))
total = 0

for i in range(1, num):
    if num % i == 0:
        total += i

if total == num:
    print("It is a Perfect Number")
else:
    print("It is not a Perfect Number")
                                                                                                                                                                                                                                                                                    