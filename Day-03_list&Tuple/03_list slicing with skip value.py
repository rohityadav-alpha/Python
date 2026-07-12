#list slicing with skip value
list1=[1,7,3,"rohit yadav",9.2,True]

print("list slicing with skip value")
print(list1[::]) #it will print all the values of list1
print(list1[:5:2]) #it will print the values of list1 from index 0 to 4 with skip value 2
print(list1[0::3]) #it will print the values of list1 from index 0 to last index with skip value 3
print(list1[0:5:1]) #it will print the values of list1 from index 0 to 4 with skip value 1
print(list1[0:5:4]) #it will print the values of list1 from index 0 to 4 with skip value 4

#string slicing with skip value operation with list
print("taken the name from list1")
name = list1[3]
print(name[::])
print(name[:5:])
print(name[:5:1])
print(name[1:5:])
print(name[1::2])
