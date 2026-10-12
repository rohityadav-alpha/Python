# 18. Find the intersection of Two Lists
list1 = [1, 2, 3]
list2 = [3, 4, 5]
inter=[]
for n1 in list1:
    for n2 in list2:
        if n1==n2:
            inter.append(n1)
print(inter)    