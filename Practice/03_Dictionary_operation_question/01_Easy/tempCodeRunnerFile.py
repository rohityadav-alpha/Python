# 20. Find the total count of a specific value's occurrences across all keys in a dictionary.
dict5={'a':5,'b':5,'c':3}
target=5
count=0
for v in dict5.values():
    if v==target:
        count+=1
print(count)