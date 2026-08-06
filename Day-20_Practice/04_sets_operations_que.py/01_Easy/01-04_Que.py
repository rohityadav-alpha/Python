# 1. Find the union of two sets.
s1={1, 2, 3, 4, 5}
s2={4, 5, 6, 7, 8}
Union=s1.union(s2)
print(Union)
# 2. Find the intersection of two sets.
Intersection=s1.intersection(s2)
print(Intersection)
# 3. Find the difference between two sets.
Diff=s1.difference(s2)
print(Diff)
# 4. Check if one set is a subset of another.
SUb=s1.issubset(s2)
print(SUb)
# 5. Find the symmetric difference of two sets.
sim=s1.symmetric_difference(s2)
print(sim)

# 6. Remove duplicate elements from a list using a set.
list1=[2,4,6,1,8,5,4,]
print(set(list1))