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