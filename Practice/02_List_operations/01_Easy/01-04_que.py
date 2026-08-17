#1. Find the Sum of All Elements in a List
list1=[6,4,8,3,1,6]
def Sum(l:list):
    sum=0
    for i in l:
        sum+=i
    return print(sum)
Sum(list1)

#2. Find the Largest and Smallest Element in a List
def Lg(l1:list):
    largest=l1[0]
    smallest=l1[0]
    for i in l1:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
    return print(largest,smallest)
Lg(list1)
            
#3. Reverse a List Without Using the Built-in reverse() Method
list1=[1,6,4,8,3,6]
def Reverse(l1:list):
    rev=[]
    for i in range(len(l1)-1,-1,-1):
        rev.append(l1[i])
    return print(rev)
Reverse(list1)

#4. Remove Duplicate Elements From a List
# solution 1 using set() method
def Duplicate(l1:list):
    new=set()
    for i in l1:
        new.add(i)
    return print(list(new))
Duplicate(list1)
# solution 2 without using set() method
li1=[4,9,'h',8,'r',3,'o',3,4,'r']
temp=[]
for i in li1:
    if i not in temp:
        temp.append(i)
print(temp)


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

#5. seperate different type of elements from the list 
# solution 1 -- using isinstance() method
l=[1,'b',7,'c',5,4,'r',7,4,'c']
int_list=[]
str_list=[]
for i in range(len(l)):
    if isinstance(l[i],str):
        str_list.append(l[i])
    elif isinstance(l[i],int):
        int_list.append(l[i])
print(int_list)
print(str_list)
print()
# solution 2 -- without isinstance() method using type() method
int_list1=[]
str_list1=[]
for i in range(len(l)):
    if type(l[i])==str:
        str_list1.append(l[i])
    elif type(l[i])==int:
        int_list1.append(l[i])
print(int_list1)
print(str_list1)