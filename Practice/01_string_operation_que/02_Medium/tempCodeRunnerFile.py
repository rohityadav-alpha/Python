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