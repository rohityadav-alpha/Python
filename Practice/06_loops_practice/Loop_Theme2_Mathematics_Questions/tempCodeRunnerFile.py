# solution 2 -- without converting
def Sum1(n):
    s=0
    for i in range(len(str(n))):
        s+=n%10
        n=n//10
    return s
print(Sum1(456))