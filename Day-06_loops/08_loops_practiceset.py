#Q1.write a program to print multiplication table of a given number using for loop
'''num=int(input("Enter the number"))
for i in range(1,11):
    print(f"{str(num)} X {str(i)} = {i*num}")

#Q2.write a program to greet all the person names stored in a list and which atert with s
l1=["rohit","shubham","vikas","ashish","kuldeep"]
for name in l1:
    if name.startswith("s"):
        print(f"Good afternoon {name}")
    

#Q3.Attempt problem 1 using while loop
num=int(input("enter the number:"))
i=0
while i<10:
    i+=1
    print(f" {num} X {i} = {num*i}")

#Q4.white a program to find whether a given number is prime or not

prime=True
for i in range(2,num):
    if num%i==0:
        prime=False
        break
if prime:
    print("the is prime number")
else:
    print("the is not prime number")

#Q5.write a program to print prime number
endval=int(input("Enter the num"))
for num in range(2,endval):
    for i in range(2,num):
        if num%i==0:
            break
    else:
        print(num)
    

#Q6.write a program to fibonacci series
#using for loop
num1=int(input("enter the number"))
a,b=0,1
for i in range(num1):
    print(a)
    a,b=b,b+a
    
num1=int(input("enter the number"))
#using while loop
a1,b1=0,1
i=0
while i<num1:
    print(a1)
    a1,b1=b1,a1+b1
    i+=1
    
#Q7.write a program to print factorial of a number
#using for loop
num=int(input("enter the number"))
strt=1
if num>0:
    for i in range(1,num+1):
        strt=strt*i
    print(strt)
#using while loop
num1=int(input("enter the number"))
strt1=1
if num1>0:
    i=1
    while i<num1:
        strt1*=i
        i+=1
    print(strt)


#perfect number is a positive integer that is equal to the sum of its proper positive divisors, excluding the number itself. For example, 6 is a perfect number because its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6.
num1=int(input("enter the number"))
div=0
for i in range(1,num1):
    if num1%i==0:
        div+=i
if num1==div:
    print("the number is a perfect number")
else:
    print("the number is not a perfect number")
'''