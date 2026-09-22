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
#solution2 - this is the solution
def Compress(s):
    s1=list(s)
    s2=""
    count=1
    for i in range(1,len(s1)):
        if s1[i]==s1[i-1]:  #if recent char is same as previous char then increase count by 1
            count+=1
        else:
            s2+=s1[i-1]+str(count) # if not then concate previous char into the empty string
            count=1
    s2+=s1[-1]+str(count)   # for last value concatinate
    return s2
print(Compress("RRohhRit"))


# 9. Decompress a Run-Length Encoded String
# solution 1
def deCompress(s):
    digit=[]
    char=[]
    result=""
    for ch in s:
        if ch.isdigit():
            digit.append(ch)
        else:
            char.append(ch)
    for i in range(len(digit)):
        result+=char[i]*int(digit[i])
    return result
print(deCompress("r2o1h3i1"))
