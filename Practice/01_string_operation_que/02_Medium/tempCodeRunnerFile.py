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