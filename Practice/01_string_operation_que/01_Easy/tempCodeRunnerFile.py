char=input("Enter the char")
try :
    print(f" the string contain only digit{int(char)}")
except ValueError:
    print("the string contain letters of alphabets")

n=char.isdigit()
print(n)