# 4. Find all elements that appear more than once in a list.
list4=[2,4,7,9,8,1,2,3,6,7,8,9,5,4,8]
duplidict={}
singledict={}

for i in list4:
    count=0
    for n in list4:
        if i==n:
            count+=1
    if count>=2:
        duplidict[i]=count
    elif count==1:
        singledict[i]=count
print(duplidict)
print(singledict)