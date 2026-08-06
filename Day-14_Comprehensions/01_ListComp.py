# list1=[] -- this is a normal way to create a list of even numbers from 0 to 20
# for i in range(20):
#     if i%2==0:
#         list1.append(i)
# print(list1)
list2=[i for i in range(20) if i%2==0] #--this is a list comprehension way to create a list of even numbers from 0 to 20
print(list2)


#square od number 1-10
list3=[i**2 for i in range(11)] #--i**2 is the square of i and for i in range(11) is the loop which will iterate from 0 to 10
print(list3)

#store characters of hello word in list
list4=[ch for ch in "hello"]
print(list4)

#convert all words in list 4 into uppercase
list4=['rohit','rahul','rohit','rohit','rahul']
list4=[i.upper() for i in list4 ]
print(list4)
list5=['ROHIT', 'RAHUL', 'ROHIT', 'ROHIT', 'RAHUL']
list5=[ch.lower() for ch in list5]
print(list5)

# filter number divisibal by 3 
list6=[i for i in range(20) if i%3==0]
print(list6)

#square only odd numbers
Odd=[i**2 for i in range(20) if i%2!=0]
print(Odd)

# flattend a nested list
nested = [[1,2],[3,4],[5,6]]
flat=[j for i in nested  for j in i]
print(flat)