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


       
# 4. Remove Duplicate Characters While Preserving Order
def removedup(s):
    word=""
    for ch in s:
        if ch not in word:
            word+=ch
        else:
            continue
    return word
print(removedup("roohitt"))



# 5. Check Whether Two Strings Are Anagrams
def anagrams(s1,s2):
    def fre(s):
        ndict={}
        for ch1 in s:
            count=0
            for ch2 in s:
                if ch1==ch2:
                    count+=1
            ndict[ch1]=count
        return ndict
    if len(s1)==len(s2) and fre(s1)==fre(s2) and set(s1)==set(s2):
        return (f"the shtrings {s1} and {s2} are anagrams")
    else:
        return (f"the shtrings {s1} and {s2} are not anagrams")
print(anagrams("listen","silent"))
print(anagrams("hello","world"))
print(anagrams("rohit","ohtri"))