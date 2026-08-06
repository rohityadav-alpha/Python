#Write a function to count the number of vowels in a string.
def Vovel(st:str)->int:
    
    num=0
    i=1
    for i in len(st):
        if 'a' in st:
            num+=i
        if 'e' in st:
            num+=i
        if 'i' in st:
            num+=i
        if 'o' in st:
            num+=i
        if 'u' in st:
            num+=i
    return num
print(Vovel("rohit"))