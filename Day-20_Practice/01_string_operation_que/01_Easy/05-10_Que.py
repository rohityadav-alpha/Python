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