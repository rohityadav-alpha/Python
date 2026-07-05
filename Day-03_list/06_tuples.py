#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Tuples are used to store multiple items in a single variable.
#The tuple() constructor can be used to create a tuple.
t=(1,4,4,5)
print(t)
print(type(t))

t1=() #empty tuple
print(t1)

#tuple methods
print("tuple methods")
print(t.count(4))
print(t.index(4))
