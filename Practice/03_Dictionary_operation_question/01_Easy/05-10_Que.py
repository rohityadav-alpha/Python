# 5. Invert a dictionary (swap keys and values).
dict1={'name':'rohit',
       'age':22,
      'subject':'maths'}
# solution 1 -- basic logics
def swap(d):
    keyL=[]
    valL=[]
    ndict={}
    for key in d.keys():
        keyL.append(key)
    for val in d.values():
        valL.append(val)
    for i in range(len(keyL)):
        ndict[valL[i]]=keyL[i]
    return ndict
print(dict1)
print(swap(dict1))
# solution 2
def Swap(d):
    ndict={}
    for k,v in d.items():
        ndict[v]=k
    return ndict
print(Swap(dict1))
# solution 3 dict comprehension
dict2={v:k for k,v in dict1.items()}
print(dict2)


# 6. Remove a key from a dictionary safely without raising an error if it doesn't exist.
# solution 1
dict1={'name':'rohit',
       'age':22,
      'subject':'maths'}
def dictCleaner(d,k):
    ndict={}
    if k not in d.keys():
        return(f"the key : {k} is not present")
    elif k in d.keys():
        for key,val in d.items():
            if key==k:
                continue
            else:
                ndict[key]=val
        return ndict
print(dictCleaner(dict1,'items'))
# solution 2
def dC(d,k):
    d.pop(k,None) #if the key is not present in the dictionary it return none nnot error
    return d
print(dC(dict1,'age'))


# 7. Sort a dictionary by its values.
dict3={'maths':97,
       'physics':66,
       'geography':58,
       'chemistry':76,
       'biology':58}
def Sort(d):
    ndict={}
    klist=[]
    for val in d.values():
        klist.append(val)
    klist.sort()
    for vl in klist:
        for k,v in d.items():
            if vl==v:
                ndict[k]=v
    return ndict
print(Sort(dict3))
dict3 = {'a':1, 'b':1, 'c':2}
print(Sort(dict3))


# 8. Check if a key exists in a dictionary.
dict3={'maths':97,
       'physics':66,
       'geography':58,
       'chemistry':76,
       'biology':58}
def checkIfValIsPresent(d,v):
    if v not in d.values():
        return (f"the value: {v} is not present in the dictionry")
    else:
        return (f"the value: {v} is present in the dictionary")
print(checkIfValIsPresent(dict3,76))


# 9. Find the sum of all values in a dictionary.
dict3={'maths':97,
       'physics':66,
       'geography':58,
       'chemistry':76,
       'biology':58}
def d_sum(d):
    return sum(d.values())
print(d_sum(dict3))


# 10. Create a dictionary from two separate lists (keys and values).
list1=['maths','physics','geography','chemistry']
list2=[83,97,88,99]
# solution 1
def combine(l1,l2):
    ndict={}
    for k,v in zip(l1,l2):
        ndict[k]=v
    return ndict
print(combine(list1,list2))
# solution 2
def Com(l1,l2):
    return dict(zip(l1,l2))
print(Com(list1,list2))