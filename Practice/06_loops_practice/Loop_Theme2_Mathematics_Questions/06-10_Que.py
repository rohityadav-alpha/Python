# 6. [Medium] Find the GCD of two numbers using a loop (without recursion or math.gcd).
# solution 1
def GCD(a,b):
    gcd=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
print(GCD(15,12))






