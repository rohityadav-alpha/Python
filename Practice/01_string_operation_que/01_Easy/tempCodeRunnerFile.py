# 11. Sort the Characters of a String Alphabetically
char=input("Enter the word: ")
def sortString(w):
    nstr=""
    list1=list(w)
    list1.sort()
    for ch in list1:
        nstr+=ch
    return nstr
print(sortString(char))