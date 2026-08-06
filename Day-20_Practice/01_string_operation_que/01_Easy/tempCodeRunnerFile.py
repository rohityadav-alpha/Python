# 7. Count Occurrences of a Given Character
def CountGivenChar(word,char):
    n=0
    for ch in word:
        if ch==char:
            n+=1
    return print(f"the number of {char} in Word:'{word}' is {n}")
CountGivenChar("BSDDIUAugiuuguageahfhghshHGUIRHSGURHTUGHDVhuhgshhghjjdj33445@@*&*^%EJWH$%*($#&FW)","I")