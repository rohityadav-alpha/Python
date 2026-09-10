num1 = int(input("enter the number"))  # take input for how many terms needed
a, b = 0, 1  # first two fibonacci numbers
for i in range(num1):  # loop num1 times
    print(a)  # print current fibonacci number
    a, b = b, b + a 