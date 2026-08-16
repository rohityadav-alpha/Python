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