# 11. Find the Index of the First Occurrence of an Element
list1=[5,7,2,4,1,3,6,9,8,4]
list2=[1,'b',7,'c',5,4,'r',7,4,'c']
# solution 1 -- for list with same type of data 
def frst_oc(l,ta):
    for i in range(len(list1)):
        if l[i]==ta:
            return (f"the element {ta} is present at {i} index in the given list")
    return (f"the element {ta} is not present in the given list {l}")
print(frst_oc(list1,4))
# solution 2 -- for list with diff type of data 
def first_Ocur(l,ta):
    for el in range(len(l)):
        if isinstance(l[el],str):
            if l[el]==ta:
                return (f"the element {ta} is present at {el} index in the given list")
        elif isinstance(l[el],int):
            if l[el]==ta:
                return (f"the element {ta} is present at {el} index in the given list")
    return (f"the element {ta} is not present in the given list {l}")
print(first_Ocur(list2,'b'))   