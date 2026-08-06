#1. Count the character of a string using a dictionary.
word=input("Enter the word: ")
def Count(word):
    ch=0
    dict1={}
    for i in word:
        ch+=1
    dict1[word]=ch
    return dict1
print(Count(word))
#1.1function to count frequence of single character in string
def Cout(w,char):
    n=0
    for ch in w:
        if char==ch:
            n+=1
    return n  
#1. Count the frequency of each character in a string using a dictionary.
def FQ(w):
    dictn={}
    for ch in w:
        dictn[ch]=Cout(w,ch) #we use  solution 1.1 to get character count
        # dictn[ch]=w.count(ch) #we use inbuild function to get character count
    return dictn
print(FQ(word))



#2. Merge two dictionaries into one.
dict2={'rohit':23,'shubham':31,'vikas':22}
dict3={'maths':88,'science':55,'english':66}
# solution 1
dict2.update(dict3) #update function use to update add new key:value pair and merge 2 differnt dictionary
print(dict2)
# solution 2
def CON(d1,d2):
    u_dict={**d1,**d2}  # **dict 2 start use to unpack dictionary
    return u_dict
print(CON(dict2,dict3))


# 3. Find the key with the maximum value in a dictionary.
def maxVal(d):
    dictn={}
    num=0
    for val in d.values(): #it returns max values
        if val>num:
            num=val
    for key in d.keys(): 
        if d[key]==num:  #if the dictionaries key's value is equal to max value
            dictn[key]=num   # store that key with max value in empty dictionary
            return dictn
print(maxVal(dict2))
print(maxVal(dict3))


# 4. Check if two dictionaries are equal.
D1={'rohit':23,'shubham':31,'vikas':22}
D2={'rohit':23,'shubham':31,'vikas':22}
def EQ(d1,d2):  
    if d1==d2:
        return print("the dict are equal")
    else:
        return print("not equal")
EQ(D1,D2)

