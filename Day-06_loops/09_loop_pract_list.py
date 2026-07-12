#Q1.write a program to Greet names starting with 's'
l1 = ["rohit", "shubham", "vikas", "ashish", "kuldeep"]  # list of names
for name in l1:  # loop through each name in the list
    if name.startswith("s"):  # check if name starts with 's'
        print(f"Good afternoon {name}")  # greet if it starts with 's'

#Q2.write a program to print even and odd numbers from a list
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # list of numbers
even = []  # empty list to store even numbers
odd = []   # empty list to store odd numbers
for num in l2:  # loop through each number in the list
    if num % 2 == 0:  # check if number is even
        even.append(num)  # add it to even list
    else:
        odd.append(num)   # add it to odd list
print(f"Even numbers: {even}")  # print even numbers
print(f"Odd numbers: {odd}")   # print odd numbers


#Q3.write a program to print prime numbers from a list
l3 = [2, 3, 4, 5, 6, 7, 8, 9, 10]  # list of numbers
primes = []  # empty list to store prime numbers
for num in l3:  # loop through each number in the list
    if num > 1:  # check if number is greater than 1
        for i in range(2,num):  # check for factors from 2 to sqrt(num)
            if num % i == 0:  # if divisible by any number
                break  # not prime, exit inner loop
        else:
            primes.append(num)  # if no factors found, it's prime
print(f"Prime numbers: {primes}")  # print prime numbers

