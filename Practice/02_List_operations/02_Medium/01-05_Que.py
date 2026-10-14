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
