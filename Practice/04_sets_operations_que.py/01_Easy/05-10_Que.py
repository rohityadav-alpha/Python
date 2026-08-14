s1={1, 2, 3, 4, 5}
s2={4, 5, 6, 7, 8}
# 5. Find the symmetric difference of two sets.
sim=s1.symmetric_difference(s2)
print(sim)

# 6. Remove duplicate elements from a list using a set.
list1=[2,4,6,1,8,5,4,]
print(set(list1))

# 7. Check if two sets are disjoint.
print(s1.isdisjoint(s2))

# 8. Add multiple elements to a set.
s3={7,83,9,5,1,6}
s1.update(s3)
print(s1)

# 9. Find common elements among three sets.
print(s1.intersection(s3,s2))

# 10. Find the maximum and minimum elements in a set.
# solution 1
def maxmin(s):
    sl=list(s)
    largest=sl[0]
    smallest=sl[0]
    for i in sl:
        if i>largest:
            largest=i
        elif i<smallest and smallest<largest:
            smallest=i
    return (f"the largest value of the set is : {largest} , and smallest is : {smallest}")
print(maxmin(s3))
# solution 2
def MaxMin(s):
    return max(s),min(s)
print(MaxMin(s3))

# 11. Convert a string into a set of unique characters.
s5="rohit roshan ravi"
def convert(s):
    return set(s)
print(convert(s5))