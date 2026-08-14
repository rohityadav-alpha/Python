# 1. Create a tuple and access its first and last elements.
t1=(1,5,4,7,3,8,5,3)
t2=(t1[0],t1[-1])
print(t2)
# 2. Count how many times an element appears in a tuple.
print(t1.count(5))
# 3. Find the index of an element in a tuple.
print(t1.index(3))
# 4. Convert a list into a tuple.
l1=[2,7,6,4,9,4]
t2=tuple(l1)
print(t2)