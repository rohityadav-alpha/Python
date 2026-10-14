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
listn=[n for n in range(1,11) if n!=4 ]
last=listn[-1]
total=last*(last+1)/2
SUM=sum(listn)
result=total-SUM
print(result) #4
