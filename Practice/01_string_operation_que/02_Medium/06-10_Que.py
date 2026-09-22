# 6. Count the Frequency of Each Word in a Sentence
def freqOfWord(sentences):
    ndict={}
    sen=sentences.split()
    for word in sen:
        count=0
        for word1 in sen:
            if word==word1:
                count+=1
        ndict[word]=count
    return ndict
print(freqOfWord("Count the Frequency of Each Word in Count the Frequency Word in Sentence"))

# 7. Find the Most Frequent Character in a String
def mostFreq(sentences):
    ndict={}
    sen=sentences.split()
    for word in sen:
        count=0
        for word1 in sen:
            if word==word1:
                count+=1
        ndict[word]=count
    result={}
    large=max(ndict.values())
    for key,val in ndict.items():
        if large==val:
            result[key]=val
    return result
print(mostFreq("Count the Frequency of Each Word in Count the Frequency Word in Sentence Word"))
    

# 8. Compress a String Using Character Counts
# solution 1 -- count characters from anywhere this is not the solution 
def compress(s):
    s2=""
    for ch in s:
        count=0
        for ch1 in s:
            if ch==ch1:
                count+=1
        if ch not in s2:
            s2=s2+ch+str(count)
    return s2
print(compress("rohito"))
