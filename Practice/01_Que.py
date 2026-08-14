#Write a Python function to check if a given integer is even or odd.
#solution 1 
num=int(input("enter the number"))
def even_odd1(num):
    if num%2==0:
        return True
    else:
        return False

if even_odd1(num) is True:
    print("even num")
else:
    print("odd num")

#solution 2
def even_odd2(num):
    if num%2==0:
        return print(f"the number {num} is even")
    else:
        return print(f"the number {num} is odd")

even_odd2(num)

#solution 3
n=int(input("enter the number"))
def even_odd3(n)->bool:
    return n%2==0 
if even_odd3(n) is True:
    print(f"the number {n} is even")
else:
    print(f"the number {n} is odd")


