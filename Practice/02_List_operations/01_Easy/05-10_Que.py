# 5. Count the Occurrences of a Given Element in a List
list2=[3,5,6,8,1,4,2,7,9,"R","rohit","R","r","&","^","#","&","r"]
def Occ(l,el):
    n=0
    for e in l:
        if el==e:
            n+=1
    return print(f"the number of character 'el' is: {n}")
Occ(list2,"&")

# 6. Check Whether a List Contains a Given Element
list2=[3,5,6,8,1,4,2,7,9,"R","rohit","R","r","&","^","#","&","r"]
def Occ(l,el):
    found=False
    for e in l:
        if e==el:
            found=True
    return found
if Occ(list2,"o") is True:
    print(f"yes! the element is present in list")
else:
    print(f"no! the element is not present in list")


# 7. Find the Second Largest Element in a List
list3=[3,5,6,8,1,4,2,7,9]
def secondLargest(l:list):
    la=0
    sl=0
    for el in l:
        if el>la:
            la=el
    for el in l:
        if el<la and el>sl:
            sl=el
    return print(f"the second largest number is: {sl}")
secondLargest(list3)

# 9. Find the Common Elements Between Two Lists
li1=['r','v',8,3]
li2=[5,6,9,2,1,3,7,'r']
def common(l1,l2):
    nlist=[]
    for i in l1:
        for j in l2:
            if j==i:
                nlist.append(j)
    return print(nlist)
common(li1,li2)

# 10. Merge Two Lists Into One Without Duplicates
# solution 1 using set() method 
li1=['r','v',8,3,3]
li2=[5,6,9,2,1,3,7,'r',6]
def mergeList(l1,l2):
    s=set(l1)
    s=set(l2)
    return print(list(s))
mergeList(li1,li2)
# solution 2 without using set method
li1=[4,9,'h',8,'r',3,'o',3,4,'r']
li2=['o',9,3,7,'i',1,'i',9,'r','t','t']
def removeDuplicate(l1,l2):
    nlist=[]
    for i in l1:
        if i not in nlist:
            nlist.append(i)
    for j in l2:
        if j not in nlist:
            nlist.append(j)
    return print(nlist)
removeDuplicate(li1,li2)


