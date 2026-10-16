# 18. Find the minimum value in a dictionary along with its key.
dict3={'maths':88,'science':55,'english':66}
maxval=0
for k,v in dict3.items():
    if v>maxval:
        maxval=v
print(maxval)