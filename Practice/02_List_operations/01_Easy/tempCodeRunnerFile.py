# 13. Flatten a Nested List (One Level Deep)
nested = [[1, 2], [3, 4], [5, 6]]
flat=[]
for n in nested:
    for e in n:
        flat.append(e)
print(flat)