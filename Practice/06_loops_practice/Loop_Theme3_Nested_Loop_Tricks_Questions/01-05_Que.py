list1=[1,4,2,5,7,8,9,5,4,3,6,7,2,3,1,9,8,6,5,1,7,7]
list2=[2,1,3,4,6,5,9,8,7]
# 1. [Easy] Count how many times a element appers in a list 
def apper(l):
    l1=set(l)
    for i in l1:
        s=0
        for j in l:
            if j==i:
               s+=1
        print(f"{i} appers {s} times in the list")
apper(list1)

print()
# 1. [Easy] Count how many pairs in a list sum to a given target using nested loops.
# solution 1 -- none repetive element
def pair(l,n):
    l1=set(l)
    s=0
    for i in l1:
        for j in l1:
            if i+j==n:
               s+=1
               print(f"{i} + {j} == {n}")
    return s
print(pair(list1,6))
print()
# solution 2 ---- with repetive element
def pair(l,n):
    l1=set(l)
    s=0
    for i in l1:
        for j in l1:
            if i+j==n:
               s+=1
               print(f"{i} + {j} == {n}")
    return s
print(pair(list1,6))
print()
# solution 3 -- according to que with repetive element
def pair_count(l,n):
    s=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
               s+=1
               print(f"{l[i]} + {l[j]} == {n}")
    return s
print(pair_count(list1,6))