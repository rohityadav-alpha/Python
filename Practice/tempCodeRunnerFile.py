# remove adjecent character from string
def removeAdj(s):
    s1=list(s)
    s2=""
    for i in range(len(s1)):
        if s1[i] not in s2:
            s2+=s1[i]
    return s2
print(removeAdj("aaabccdc"))