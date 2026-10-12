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



# 18. Find the Union of Two Lists
union_list = list(set(list1) | set(list2))
print(union_list) # [1, 2, 3, 4, 5]

# 19. Find the intersection of Two Lists
list1 = [1, 2, 3]
list2 = [3, 4, 5]
inter=[]
for n1 in list1:
    for n2 in list2:
        if n1==n2:
            inter.append(n1)
print(inter)      



# 20. Remove All Occurrences of a Given Element From a List
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
result = []

for num in numbers:
    if num != target:
        result.append(num)

print(result) # [1, 3, 4, 5]