#sets methods

#add elements in set
a =set()
a.add(1)
a.add(3)
a.add(4)
a.add(7)
a.add((5,6))   #tuples are immutable, so they can be added to a set
#a.add({})      --this return error , cannot add dictionary in set ,dict is mutable
#a.add([2,3,4,9]--this return error , cannot add list in set ,list is mutable
#a.add(3,4,7)   --it return error , you can add 1 element at a time
#a.add(3)       --it return error , 3 is present in set because set is a collection of  non repetative element
print(type(a))
print(a)

print("\n")

#remove elements from sets
b ={3,4,5,6,8}
b.remove(3)
#b.remove()    --it return error , you have to put one element to remove
#b.remove(3,4) --it return error , you can remove one element at a time
print(b)

print("\n")

#Remove random element from the the set 
c ={2,4,7,9}
c.pop()
#c.pop(7)      --it return error , dont need to define element to remove mostly from end of the set of the last one add 
print(c)

print("\n")

#Clear the entire set , remove all elements from the set
d ={5,0,3,1}
d.clear() #it return empty set : set()
print(d)

print("\n")

#union set --it returns all elements from both sets 
e = a.union(b)  #e is a new variable to store union elements
print(e)

print("\n")

#intersection set --it return similar value from both set
f = a.intersection(b)  #f is a new variable to store intersection elements
print(f)
