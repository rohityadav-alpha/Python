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