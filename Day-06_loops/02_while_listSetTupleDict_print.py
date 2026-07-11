#Write a program to print list element
list1=[1,4,6,3,7,"rohit",True,False]
i=0
while i<len(list1):
    print(list1[i])
    i+=1

#Write a program to print list element in reverse order
list4=[1,4,6,3,7,"rohit",True,False]
list4.reverse()
i=0
while i<len(list4):
    print(list4[i])
    i+=1

#write a program to print list element in reverse order without using reverse() method
list2=[1,4,6,3,7,"rohit",True,False]
list2=list2[::-1]
i=0
while i<len(list2):
    print(list2[i])
    i+=1

#write a program to print tuple element
tuple1=(1,4,6,3,7,"rohit",True,False)
i=0
while i<len(tuple1):
    print(tuple1[i])
    i+=1


#write a program to print dictionary element
dict1={"name":"rohit","age":22,"city":"delhi"}
i=0
while i<len(dict1):
    key=list(dict1.keys())[i]
    print(key,":",dict1[key])
    i+=1

#write a program to print set element
set1={1,4,6,3,7,"rohit",True,False}
i=0
while i<len(set1):
    print(list(set1)[i])
    i+=1

