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