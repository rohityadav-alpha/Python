# 11. Sort the Characters of a String Alphabetically
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
