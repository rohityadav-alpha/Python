# iterable - An object which will return an iterator when iter() is called on it. It implements the __iter__() method.
# iterator - An object which will return the next value when next() is called on it. It implements the __next__() method.
# iteration - The process of iterating over an iterable object using an iterator object. It is done using a for loop or by calling the next() function on the iterator object.

#Iterable = object has contain data (list,tuple,string etc).
name="rohit"
print(name)

print("\n")
#Iterator = tool that extract data one by one after calling.
n=iter(name)
print(next(n))
print(next(n))
print(next(n))
print(next(n))

print("\n")

#Iteration = a process in where you traverse data at once .
for n in name:
    print(n)
