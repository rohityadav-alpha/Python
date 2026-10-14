# find the second largest number in the list
list1=[5, 3, 9, 1, 4]
first=0
second=0
for n in list1:
    if n>first:
        first,second=n,first
print(second)


# 1. Find the second smallest element in a list without using sort().
list1=[5, 3, 9, 1, 4]
first=list1[0]
second=0
for n in list1:
    if n<first:
        first,second=n,first
print(second)



# 2. Find the missing number in a list of 1 to N.
list2=[n for n in range(1,11) if n!=4 ]
last=list2[-1]
total=last*(last+1)/2
SUM=sum(list2)
result=total-SUM
print(result) #4




# 3. Split a list into chunks of size K.
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