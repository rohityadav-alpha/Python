# 8. [Medium] Check whether a number is an Armstrong number (sum of cubes/nth powers of digits equals the number).
def armstrong(n):
    n1=str(n)
    num=n
    Sum=0
    for i in n1:
        digit=n%10
        Sum+=digit**(len(n1))
        n=n//10
    if Sum==num:
        return (f"the number is armstrong")
    else:
        return (f"the number is not armstrong")
print(armstrong(9474))