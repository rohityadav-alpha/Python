# 5. Rotate a list to the right by K positions in-place.
list5=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
def rotate(l,k):
    nlist=l[k:]+l[0:k]
    return nlist
print(rotate(list5,10))