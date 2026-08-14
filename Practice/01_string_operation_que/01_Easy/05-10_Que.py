# 5. Count Vowels and Consonants
def CountVovelConsonent(w:str)->int:
    v=0
    c=0
    for ch in w:
        if ch in "aeiou":
            v+=1
        else:
            c+=1
    return print(f"number of vovels is: {v} and number of consonent is: {c}")
CountVovelConsonent("agjhhdewotuiufhjdjbcxvcnxvkddsreyreyhdhgsvgacgftedqtrewefdgd")


# 6. Count Uppercase, Lowercase, Digits, and Special Characters
def CountStringCharacter(w):
    U=L=S=D=0
    for ch in w:
        if ch.isupper():
            U+=1
        elif ch.islower():
            L+=1
        elif ch.isdigit():
            D+=1
        else:
            S+=1
    return print(f"number of Uppercase characters is: {U}\nnumber of Lowercase characters is: {L}\nnumber of Special characters is: {S}\nnumber of Digit characters is: {U}")
CountStringCharacter("BSDDIUAugiuuguageahfhghshHGUIRHSGURHTUGHDVhuhgshhghjjdj33445@@*&*^%EJWH$%*($#&FW)")


# 7. Count Occurrences of a Given Character
def CountGivenChar(word,char):
    n=0
    for ch in word:
        if ch==char:
            n+=1
    return print(f"the number of {char} in Word:'{word}' is {n}")
CountGivenChar("BSDDIUAugiuuguageahfhghshHGUIRHSGURHTUGHDVhuhgshhghjjdj33445@@*&*^%EJWH$%*($#&FW)","I")

# 8. Remove All Spaces from a String
name="rohit kumar  yadav"
# solution 1
print(name.replace(" ",""))
# solution 2
def RemoveSpace(w):
    nch=""
    for ch in w:
        if ch!=" ":
            nch=nch+ch
    return str(nch)
print(RemoveSpace(name))


# 9. Swap the First and Last Character of a String
subject=input("Enter the word: ")
def swap(w):
    if len(w)>2:
       t=w[0]
       t1=[-1]
       nw=""
       for i in range(len(w)):
            if i==0:
               nw+=w[-1]
            elif i==(len(w)-1):
               nw+=w[0]
            else:
                nw+=w[i]
    return nw
print(swap(subject))
# solution 2
nw=""
if len(subject)<2:
    nw=subject
else:
    nw=subject[-1]+subject[1:-1]+subject[0]
print(nw)


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
    # word=w.split() #this metehod use to split words from sentence and store into list
    word=split(w) #this is a custom split function at line 83
    new_sen=""
    for ch in word:
        new_sen+=ch.capitalize()+" "
    return new_sen
print(cap(letter))



