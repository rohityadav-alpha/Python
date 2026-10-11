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



# 17. Find the Average of Elements in a List
numbers = [10, 20, 30, 40]
def Avg(l):
    a=sum(l)/len(l)
    return a
print(Avg(numbers))