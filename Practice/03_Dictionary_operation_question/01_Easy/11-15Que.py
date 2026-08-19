# 11. Find all keys in a dictionary whose values are greater than a given threshold.
dict1={'maths':97,
       'physics':66,
       'geography':58,
       'chemistry':76,
       'biology':58}
def above(d,n):
    nlist=[]
    for k,v in d.items():
        if v>n:
            nlist.append(v)
    return nlist
print(above(dict1,67))



# 12. Count the number of unique values in a dictionary.
dict2={'maths':97,
       'physics':66,
       'geography':58,
       'chemistry':76,
       'biology':58,
       'maths1':97,
       'physics1':66,
       'geography1':58,
       'chemistry1':76,
       'biology1':58,
       'english':66}
def uniquevalue(d):
    s=set(d.values())
    return len(s)
print(uniquevalue(dict2))



# 13. Update dictionary values by adding a fixed number to each value.
def addFixVal(d,v):
    ndict={}
    for key,val in d.items():
        ndict[key]=val+v
    return ndict
print(addFixVal(dict2,75))



# 14. Find the common keys between two dictionaries.
dict3={'maths':88,'science':55,'english':66}
# solution 1--without using set() function
def common(d1,d2):
    nlist=[]
    for key1 in d1:
        for key2 in d2:
            if key1==key2 and key1 not in nlist:
                nlist.append(key1)
    return nlist
print(common(dict2,dict3))
# solution 2--using set functions
def common1(d1,d2):
    s=set(d1.keys())
    s1=set(d2.keys())
    return s.intersection(s1)
print(common1(dict2,dict3))
# solution3--using & operator
def common2(d1,d2):
    return d1.keys()&d2.keys()
print(common2(dict2,dict3))
