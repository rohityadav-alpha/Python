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
print(freq("rrohit"))
# solution 2
text = "programming"
def frequ(s):
    ndict = {}
    for char in text:
        ndict[char] = ndict.get(char, 0) + 1
    return ndict
print(frequ(text))


# 2. Find the First Non-Repeating Character in a String
def firstnonrep(d):
    temp={}
    for key,val in d.items():
        if val==1:
            temp[key]=val
            break
    return (f"the first non repetive character is {temp}")
print(firstnonrep(freq("rrooohhitt"))) #freq() function is returns the frequency of each character from the string this is a question no.1


# 3. Find the First Repeating Character in a String
def firstrep(d):
    s={}
    for key,val in d.items():
        if val>1:
            s[key]=val
            break
    return (f"the first repeting charecter is {s}")
print(firstrep(freq("rohihit")))

