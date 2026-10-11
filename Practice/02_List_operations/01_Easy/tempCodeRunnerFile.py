list1=[5,7,2,4,1,3,6,9,8,4]
# 12. Rotate a List to the Left by K Positions
def rotate_list(l,k):
    k1=k%len(l)
    rotate=l[k1:]+l[:k1]
    return rotate
print(rotate_list(list1,5))