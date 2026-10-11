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