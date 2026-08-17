# 11. Find the Index of the First Occurrence of an Element
list1=[1,'b',7,'c',5,4,'r',7,4,'c']
def first_Ocur(l,ta):
    for el in range(len(l)):
        if isinstance(l[el],str):
            if l[el]==ta:
                return (f"the element {ta} is present at {el} index in the given list")
        elif isinstance(l[el],int):
            if l[el]==ta:
                return (f"the element {ta} is present at {el} index in the given list")
    return (f"the element {ta} is not present in the given list {l}")
print(first_Ocur(list1,'b'))   