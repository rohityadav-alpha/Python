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