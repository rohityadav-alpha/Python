# 16. Find All Positive and Negative Numbers in a List
numbers = [3, -1, 4, -5, 0, 2]
P=[]
N=[]
for n in numbers:
    if n>=0:
        P.append(n)
    elif n<0:
        N.append(n)
print(P)
print(N)
