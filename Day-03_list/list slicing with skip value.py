#list slicing with skip value
list1=[1,7,3,"rohit yadav",9.2,True]

print("list slicing with skip value")
print(list1[::])
print(list1[:5:2])
print(list1[0::3])
print(list1[0:5:])
print(list1[0:5:4])

print("taken the name from list1")
name = list1[3]
print(name[::])
print(name[:5:])
print(name[:5:1])
print(name[1:5:])
print(name[1::2])
