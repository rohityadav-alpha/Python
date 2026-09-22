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
