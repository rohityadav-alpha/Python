#list <--- is a containter use to store values of different data types
#list is a ordered collection of items which is mutable and allows duplicate members
print("list")
list1=[1,7,3,"rohit",9.2,True]
print(list1)  #it returns entire values from list
print(list1[3])   #it returns the 3rd position value from list
print(list1[-2])  #it returns the 2 value from reverce count
list1[3]="sanjay" #acces the value and change the value using position 
list1[1]=78

#list slicing
print("list slicing")
print(list1[2:]) #list1[ start_posuition : autodetect_end_position ]
print(list1[1:5]) #list1[ start_posuition : end_position ]
print(list1[-2:]) #list1[ start_posuition : autodetect_end_position ] from reverce count
print(list1[-5:-2]) #list1[ start_posuition : end_position ] from reverce count

#list slicing with skip value
print("list slicing with skip value")
print(list1[0:5:]) 
