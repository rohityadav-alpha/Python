# find the second largest number in the list
list1=[5, 3, 9, 1, 4]
first=0
second=0
for n in list1:
    if n>first:
        first,second=n,first
print(second)


