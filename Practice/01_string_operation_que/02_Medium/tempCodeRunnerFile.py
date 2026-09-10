# 1. Find the Frequency of Each Character in a String
def freq(s):
    ndict={}
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        ndict[s[i]]=count
    return ndict
print(freq("programming"))