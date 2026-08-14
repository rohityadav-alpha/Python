# 10. Capitalize the First Letter of Each Word Without Using title()
letter="dear sir rohit thanks you"
w=letter.split()
print(w)
# create our own split function
def split(s):
    list1=[]
    tw=""
    for char in s:
        if char==" " or char=="  ":
            list1.append(tw)
            tw=""
        else:
            tw+=char
    return list1
def cap(w):
    # word=w.split() #this metehod use to split sentence into words and store into list
    word=split(w) #this is a custom split function at line 83
    new_sen=""
    for ch in word:
        new_sen+=ch.capitalize()+" "
    return new_sen
print(cap(letter))



