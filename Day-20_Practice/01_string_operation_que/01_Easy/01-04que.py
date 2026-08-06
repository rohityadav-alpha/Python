#1.Find the Length of a String Without Using len()
print(len("rohit"))
def s_length(s)->int:
    len=0
    for i in s:
        len+=1
    return len
print(s_length("rohit"))

#2.Print Every Character of a String
def Char(s:str)->str:
    for i in s:
        print(i)
Char("roshni")

#3.Reverse a String Using a Loop
def Reverse(s:str):
    rev=""
    for i in range(len(s)-1,-1,-1): # (start:len(s)-1=4 , stop:-1 ,step:-1 reverse the loop)  is the last index of the string, -1 is the stop index (not included), and -1 is the step (to go backwards)
        rev+=s[i]
    return print(rev)
Reverse("vikas")

#4.Check Whether a String Is a Palindrome
def palindrome(s:str):
    rev=""
    for i in range(len(s)-1,-1,-1): 
        rev+=s[i]
    if rev==s:
       return print(f"the string {s} is palindrom")
    else:
        return print(f"the string {s} is not palindrom")
palindrome("boob")

