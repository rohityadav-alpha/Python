t1 = (1, 2, 3, 4, 5)
# 11. Repeat a tuple multiple times.
def repete(t,n):
    return t*n
print(repete(t1,2))

# 12. Find the maximum and minimum element in a tuple.
# solution 1 -- using max() and min() methods
print(max(t1))
print(min(t1))
# solution 2 -- without using max() and min() methods
def maxmin(t):
    largest=t1[0]
    smallest=t1[0]
    for i in t:
        if i>largest:
            largest=i
        elif i<smallest and smallest<largest:
            smallest=i
    return largest,smallest
print(maxmin(t1))



# 13. Convert a tuple into a list.
def con(t):
    return list(t)
print(con(t1))


# 14. Swap two variables using tuple unpacking.
def swap(a,b):
    a,b=b,a
    return a,b
print(swap(4,7))


# 15. Use a tuple as a dictionary key.
tuple1=("maths",'science','english','history')
tuple2=(56,87,45,98)
print(dict(zip(tuple1,tuple2)))
def tup(t,t1):
    dict1={}
    for i in range(len(t)):
        dict1[t[i]]=t1[i]
    return dict1
print(tup(tuple1,tuple2))


