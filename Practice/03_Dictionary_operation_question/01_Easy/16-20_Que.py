# 16. Find the length (number of key-value pairs) of a dictionary.
dict1={'maths':88,'science':55,'english':66}
count=0;
for k in dict1:
    count+=1
print(count)



# 17. Check if a dictionary is empty.
dict2={}
ct=0
for k in dict2:
    ct+=1
if ct<1 and ct==0:
    print("dictionary is empty")
else:
    print("dictionary is not empty")
# solution 2
print(not dict2) # empty dict is consider false in python



# 18. Find the minimum value in a dictionary along with its key.
dict3={'maths':88,'science':55,'english':66}
maxval=0
for k,v in dict3.items():
    if v>maxval:
        maxval=v
print(maxval)



# 19. Group a list of words by their first letter using a dictionary.
list1=['apple','ant','banana','bee']
dict4={}
for word in list1:
    dict4[word[0]]=[w for w in list1 if w[0]==word[0]]
print(dict4)