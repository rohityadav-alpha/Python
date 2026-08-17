# 11. Find the Index of the First Occurrence of an Element
list1=[5,7,2,4,1,3,6,9,8]
list2=[1,'b',7,'c',5,4,'r',7,4,'c']
# solution 1 -- for list with same type of data 
def frst_oc(l,ta):
    for i in range(len(list1)):
        if l[i]==ta:
            return (f"the element {ta} is present at {i} index in the given list")
    return (f"the element {ta} is not present in the given list {l}")
print(frst_oc(list1,4))