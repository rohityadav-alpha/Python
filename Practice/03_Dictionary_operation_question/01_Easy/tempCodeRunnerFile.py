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