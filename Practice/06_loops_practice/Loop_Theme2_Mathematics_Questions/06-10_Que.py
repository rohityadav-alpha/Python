# 6. [Medium] Find the GCD of two numbers using a loop (without recursion or math.gcd).
# solution 1
def GCD(a,b):
    gcd=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd
print(GCD(15,12))
# solution 2
def gcd(a, b):
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a
print(gcd(15, 12)) # 6



# 7. [Medium] Find the LCM of two numbers using a loop-based brute-force approach.
# solution 1
def LCM(a,b):
    gcd=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return (a*b)/gcd
print(LCM(4,6))

