# 7. [Medium] Find the LCM of two numbers using a loop-based brute-force approach.
# solution 1
def LCM(a,b):
    gcd=0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return (a*b)/gcd
print(LCM(4,6))
# solution 2
def lcm_bruteforce(a, b):
    if a == 0 or b == 0:
        return 0
    larger = max(a, b)
    candidate = larger
    while True:
        if candidate % a == 0 and candidate % b == 0:
            return candidate
        candidate += larger
print(lcm_bruteforce(4, 6)) # 12