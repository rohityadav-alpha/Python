#Q1.write a program to print multiplication table of a given number using for loop
num = int(input("Enter the number"))  # take number input from user
for i in range(1, 11):  # loop from 1 to 10
    print(f"{str(num)} X {str(i)} = {i*num}")  # print each line of the table



#Q2.write a program to print Multiplication table using while loop
num = int(input("enter the number:"))  # take number input
i = 0  # initialize counter
while i < 10:  # loop until i is less than 10
    i += 1  # increment counter first (so table goes from 1 to 10)
    print(f" {num} X {i} = {num*i}")  # print table line



#Q3.write a program to print Fibonacci series
# using for loop
num1 = int(input("enter the number"))  # take input for how many terms needed
a, b = 0, 1  # first two fibonacci numbers
for i in range(num1):  # loop num1 times
    print(a)  # print current fibonacci number
    a, b = b, b + a  # update both variables (generate next fibonacci number)

# using while loop
num1 = int(input("enter the number"))  # take input for number of terms
a1, b1 = 0, 1  # starting two numbers
i = 0  # counter
while i < num1:  # loop while count is less than num1
    print(a1)  # print current number
    a1, b1 = b1, a1 + b1  # calculate next fibonacci number
    i += 1  # increment counter


#Q4.write a program to find Factorial of a number
# using for loop
num = int(input("enter the number"))  # take number input
strt = 1  # variable to store factorial, start at 1
if num > 0:  # if number is positive
    for i in range(1, num+1):  # loop from 1 to num
        strt = strt * i  # keep multiplying each number
    print(strt)  # print final factorial

# using while loop
num1 = int(input("enter the number"))  # take number input
strt1 = 1  # factorial variable
if num1 > 0:  # check positive
    i = 1  # counter
    while i <= num1:  # FIX: was i<num1, which skipped multiplying by the last number; now i<=num1
        strt1 *= i  # keep multiplying
        i += 1  # increment counter
    print(strt1)  # FIX: was printing 'strt' (wrong variable) instead of 'strt1'


#Q5.write a program to Check perfect number
num1 = int(input("enter the number"))  # take number input
div = 0  # variable to store sum of divisors
for i in range(1, num1):  # loop from 1 to num1-1 (proper divisors)
    if num1 % i == 0:  # if i is a divisor
        div += i  # add it to the sum
if num1 == div:  # if sum equals the number itself
    print("the number is a perfect number")  # then it's a perfect number
else:
    print("the number is not a perfect number")  # otherwise not a perfect number


#Q6.write a program to Check Armstrong number
num1 = int(input("enter the number"))  # take number input
arm = 0  # variable to store armstrong sum
n_digits = len(str(num1))  # FIX: get actual digit count instead of hardcoding 3 (cube)
for i in str(num1):  # convert number to string, loop through each digit
    arm += int(i)**n_digits  # FIX: raise each digit to power(n_digits) instead of fixed power(3), works for any digit length now
if arm == num1:  # if sum equals the original number
    print("the number is an Armstrong number")  # then it's an Armstrong number
else:
    print("the number is not an Armstrong number")  # otherwise not


#Q7.write a program to Separate even and odd numbers from list
l1 = [3, 4, 9, 2, 5, 6, 7, 1, 8]  # list of numbers
even, odd = [], []  # empty lists to store even and odd numbers
for i in l1:  # loop through each number in the list
    if i % 2 == 0:  # if number is even
        even.append(i)  # add it to even list
    else:
        odd.append(i)  # otherwise add it to odd list
print(f"Even numbers: {even}")  # print even numbers
print(f"Odd numbers: {odd}")  # print odd numbers


#Q8.write a program to Sum of digits of a number
num = int(input("enter the number"))  # take number input
sum1 = 0  # variable to store sum
for i in str(num):  # convert number to string, loop through each digit
    sum1 += int(i)  # add each digit to the sum
print(sum1)  # print the total sum


#Q10.write a program to Reverse a number
# using while loop
num = int(input("enter the number"))  # take number input
rev = 0  # variable to store reversed number
while num > 0:  # loop while number is greater than 0
    digit = num % 10  # extract last digit
    rev = rev*10 + digit  # add digit to reversed number
    num = num // 10  # remove last digit from number
print(rev)  # print reversed number

# using for loop
num = int(input("enter the number"))  # take number input
rev = 0  # variable to store reversed number
temp = num  # copy of original number (since len(str(num)) is used)
for i in range(len(str(num))):  # loop as many times as digits in the number
    digit = temp % 10  # extract last digit
    rev = rev*10 + digit  # build reversed number
    temp = temp // 10  # remove last digit
print(rev)  # print reversed number


#Q9.write a program to Find prime factors of a number
num = int(input("enter the number"))  # take number input
i = 2  # start checking from the smallest prime
while i*i <= num:  # loop while i squared is less than or equal to num
    if num % i == 0:  # check if i divides num evenly
        print(i)  # if yes, i is a prime factor, print it
        num = num // i  # reduce num by dividing it by i (e.g. 12//2=6)
    else:
        i += 1  # if not a divisor, check next number
# remaining prime
if num > 1:  # FIX: if leftover num became 1 (e.g. 8 -> 2,2,2 leaves num=1), skip printing it
    print(num)  # print the remaining prime factor after the loop ends



#Q10.write a program to Check whether a number is prime or not
num = int(input("enter the number: "))  # FIX: added missing input line, 'num' was undefined before
prime = True  # assume prime initially
if num < 2:  # FIX: 0 and 1 are not prime numbers, this check was missing
    prime = False
else:
    for i in range(2, num):  # check divisors from 2 to num-1
        if num % i == 0:  # if a divisor is found
            prime = False  # then it's not prime
            break  # no need to check further, exit loop
if prime:  # if flag is still True
    print("the number is prime")  # FIX: fixed grammar from "the is prime number"
else:
    print("the number is not prime")  # FIX: fixed grammar


#Q11.write a program to Print prime numbers up to a given number
endval = int(input("Enter the num"))  # take end value input
for num in range(2, endval):  # check every number from 2 to endval-1
    for i in range(2, num):  # check divisors of num
        if num % i == 0:  # if a divisor is found
            break  # break inner loop, not prime
    else:  # runs only if inner loop completed without break (no divisor found)
        print(num)  # so num is prime, print it


#Q12.write a program to find GCD of two numbers
a = int(input("Enter first number: "))  # take first number input
b = int(input("Enter second number: "))  # take second number input
gcd = 1  # variable to store the greatest common divisor, start with 1
for i in range(1, min(a, b) + 1):  # loop from 1 to the smaller of a and b (GCD can't exceed smaller number)
    if a % i == 0 and b % i == 0:  # check if i divides both a and b evenly
        gcd = i  # if yes, update gcd (keep overwriting so the largest common divisor is kept last)
print("GCD is:", gcd)  # print the final GCD found


#Q13.write a program to find LCM of two numbers
a = int(input("Enter first number: "))  # take first number input
b = int(input("Enter second number: "))  # take second number input
# First find GCD
gcd = 1  # variable to store the greatest common divisor
for i in range(1, min(a, b) + 1):  # loop from 1 to the smaller of a and b
    if a % i == 0 and b % i == 0:  # check if i divides both a and b evenly
        gcd = i  # update gcd whenever a bigger common divisor is found
lcm = (a * b) // gcd  # LCM formula: (a times b) divided by GCD
print("LCM is:", lcm)  # print the final LCM# GCD of two numbers
