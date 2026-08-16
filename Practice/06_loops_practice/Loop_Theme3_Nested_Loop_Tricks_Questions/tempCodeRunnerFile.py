def pair_count(l,n):
    s=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]+l[j]==n:
               s+=1
               print(f"{l[i]} + {l[j]} == {n}")
    return s
print(pair_count(list1,6))