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