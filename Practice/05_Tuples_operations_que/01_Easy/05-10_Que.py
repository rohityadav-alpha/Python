# 5. Concatenate two tuples.
t1=(3,7,1,9,3)
t2=('r',7,4,'R',65.3,'roshan')
t3=t1+t2
print(t3)

# 6. Slice a tuple to get a sub-tuple.
t4=t3[2:9]
print(t4)

# 7. Unpack a tuple into variables .
# solution 1 -- unpack and stored into dictionary 
val=(5,7,3,9,6,1)
varb=('a','b','c','d','e','f')
def unpack(t,v):
    return dict(zip(v,t))
print(unpack(val,varb))
# solution 2 -- unpack simply
def Unpack(t):
    a,b,c,d,e,f,=t
    return a,b,c,d,e,f
print(Unpack(val))


# 8. Check if an element exists in a tuple.
def check(t,e):
    if e in t:
        return (f"the element {e} is present in the tuple")
    else:
        return (f"the element {e} is not present in the tuple")
print(check(t4,'R'))
print(check(t4,'f'))

# 9. Find the length of a tuple.
# solution 1-- without len() method
def Len(t):
    n=0
    for i in t:
        n+=1
    return n
print(Len(varb))
# solution 2-- eith len() method
print(len(varb))

# 10. Create a single-element tuple correctly.
t=(1,) #this is a single tuple
print(t)
print(type(t))

# 11. Repeat a tuple multiple times.
def repete(t,n):
    return t*n
print(repete(t1,2))