t1 = (1, 2, 3, 4, 5)
# 11. Repeat a tuple multiple times.
def repete(t,n):
    return t*n
print(repete(t1,2))

# 12. Find the maximum and minimum element in a tuple.
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