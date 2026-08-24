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