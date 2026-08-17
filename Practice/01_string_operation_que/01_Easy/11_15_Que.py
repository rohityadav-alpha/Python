# 11. Sort the Characters of a String Alphabetically
import re

from django.utils import text


word=input("Enter the word: ")
letter=input("Enter the leter: ")
def sortString(w):
    nstr=""
    list1=list(w)
    list1.sort()
    for ch in list1:
        nstr+=ch
    return nstr
print(sortString(word))


# 12. Find the First Index of a Given Character
def firstIndex(w,ch):
    for i in range(len(w)):
        if w[i]==ch:
            print(f"the leter {ch} appear at index {i}")
firstIndex(word,letter)


# 13. Check Whether a String Contains Only Digits
# solution 1 -- without .isdigit() method 
char=input("Enter the char")
try :
    print(f" the string contain only digit{int(char)}")
except ValueError:
    print("the string contain letters of alphabets")
# solution 2 --using .isdigit() method
n=char.isdigit()
if n:
    print("the string contain only digit")



# 14. Find the Longest Word in a Sentence
sen="dear! rohit yadav your selected for it trichi thanks!"
# solution 1
def largest_sen(sentence):
    final=0
    wd=""
    for word in sentence.split():
        current=0
        for j in word:
            current+=1
        if current>final:
            final=current
            wd=word
    return wd,final
print(largest_sen(sen))
print(sen.split())
# solution 2
words = text.split()
longest = ""
for word in words:
    if len(word) > len(longest):
        longest = word
print(longest) # programming