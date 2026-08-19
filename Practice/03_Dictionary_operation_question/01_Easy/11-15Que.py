# 11. Find all keys in a dictionary whose values are greater than a given threshold.
dict3={'maths':97,
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
print(above(dict3,67))