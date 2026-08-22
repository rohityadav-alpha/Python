
# 15. Use a tuple as a dictionary key.
tuple1=("maths",'science','english','history')
tuple2=(56,87,45,98)
print(dict(zip(tuple1,tuple2)))
def tup(t,t1):
    dict1={}
    for i in range(len(t)):
        dict1[t[i]]=t1[i]
    return dict1
print(tup(tuple1,tuple2))