letter1="dear sir,my name is rohit yadav i m writing this regard my 5 days hollidays thanks sir"
print(len(letter1))
print(letter1.endswith("sir"))
#print(letter1.center("rohit"))
print(letter1.find("rohit"))
print(letter1.replace("sir","nitin"))
print(letter1.capitalize())
#print(letter1.formate("holliday"))
print(letter1.count("sir"))
print(letter1.lower())
print(letter1.split())

list1=['dear', 'sir,my', 'name', 'is', 'rohit', 'yadav', 'i', 'm', 'writing', 'this', 'regard', 'my', '5', 'days', 'hollidays', 'thanks', 'sir']
print("".join(list1))
tuple1=('dear', 'sir,my', 'name', 'is', 'rohit', 'yadav', 'i', 'm', 'writing', 'this', 'regard', 'my', '5', 'days', 'hollidays', 'thanks', 'sir')
print("".join(tuple1))
set1={'dear', 'sir,my', 'name', 'is', 'rohit', 'yadav', 'i', 'm', 'writing', 'this', 'regard', 'my', '5', 'days', 'hollidays', 'thanks', 'sir'}
print("".join(set1))

#chr(65) is equal to A character in python Capital Alphabets are start from chr(65)=="A" and small alphabets starts from chr(97)=="a"
for i in range(26):
    print(chr(97+i))
# Using ord("") to find the value of the string character ord("A") return 65 and ord("a") return 97
val=ord("A")
vl=ord("a")
print(val,vl)