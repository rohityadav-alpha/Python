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
    return dictn
print(FQ(word))