# 20. Remove All Occurrences of a Given Element From a List
numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
result = []

for num in numbers:
    if num!=target:
        result.append(num)
        
print(result) # [1, 3, 4, 5]