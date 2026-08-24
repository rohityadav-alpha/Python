# 1. [Easy] Find the sum of digits of a number using a loop.
# solution 1 -- converting intiger into string
def Sum(n:int)->int:
    w=str(n)
    add=0
    for i in w:
        add+=int(i)
    return add
print(Sum(456))
# solution 2 -- without converting
def Sum1(n):
    s=0
    for i in range(len(str(n))):
        s+=n%10
        n=n//10
    return s
print(Sum1(456))



# 2. [Easy] Count the digits of a number without converting it to a string.
num=int(input("enter thhe number :"))
def Count(n):
    n1=0
    while n>0:
        n=n//10
        n1+=1
    return n1
print(Count(num))


# 3. [Easy] Reverse a number using a loop and check if it's a palindrome by comparing with original.
num=int(input("enter thhe number :"))
def palindrom(n):
    temp=n
    rev=0
    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    if temp==rev:
        return (f"the number is palindrom")
    else:
        return (f"the number is not palindrom")
print(palindrom(num))



# 4. [Easy] Calculate the factorial of a number using a loop.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        print(fact)
    return fact
print(factorial(5))


# 5. [Easy] Check whether a number is prime using a loop.
def prime(n):
    if n>2:
        for i in range(2,n):
            if n%i==0:
                return False
    return True
if prime(9):
    print("the number is prime number")
else:
     print("the number is not prime number")