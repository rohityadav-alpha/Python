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