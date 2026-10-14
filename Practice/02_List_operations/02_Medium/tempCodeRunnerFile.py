# soltion 1--list comprension
list3=[n for n in range(1,101)]
def chunks(l,k):
    nlist=[l[i:i+k] for i in range(0, len(l), k)]
    return nlist
print(chunks(list3,50))
# solution 2
def chunksize(l,k):
    listn=[]
    for i in range(0,len(l),k):
        listn.append(l[i:i+k])
    return listn
print(chunksize(list3,20))