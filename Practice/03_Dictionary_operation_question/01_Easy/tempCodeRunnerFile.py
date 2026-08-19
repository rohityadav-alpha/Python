# 12. Count the number of unique values in a dictionary.
dict4={'maths':97,
       'physics':66,
       'geography':58,
       'chemistry':76,
       'biology':58,
       'maths1':97,
       'physics1':66,
       'geography1':58,
       'chemistry1':76,
       'biology1':58}
def uniquevalue(d):
    s=set(d.values())
    return len(s)
print(uniquevalue(dict4))

# 13. Update dictionary values by adding a fixed number to each value.
def addFixVal(d,v):
    ndict={}
    for key,val in d.items():
        ndict[key]=v
    return ndict
print(addFixVal(dict4,75))