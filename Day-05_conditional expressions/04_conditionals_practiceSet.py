#Q1.write a program to find greatest of four numbers entered by user.
n1=int(input("Enter 1 number:"))
n2=int(input("Enter 2 number:"))
n3=int(input("Enter 3 number:"))
n4=int(input("Enter 4 number:"))
#solution1
print(max(n1,n2,n3,n4))
#solution2
if n1>n2 and n1>n3 and n1>n4:
    print(n1)
elif n2>n1 and n2>n3 and n2>n4:
    print(n2)
elif n3>n1 and n3>n2 and n3>n4:
    print(n3)
elif n4>n1 and n4>n2 and n4>n3:
    print(n4)
#solution3
greatest = n1
if n2 > greatest:
    greatest = n2
if n3 > greatest:
    greatest = n3
if n4 > greatest:
    greatest = n4
print(greatest)



#Q2.write a program to find out whether a student is pass or fail if it requires total 40% and atleast 33% in each subject to pass assume 3 subjects and take marks as an input from the user
s=int(input("Enter the marks of science"))
m=int(input("Enter the marks of maths"))
e=int(input("Enter the marks of english"))
overall=s+m+e
marks=100
if s>33 and s<=100:
    print("pass in science")
else:
    print("fail  in science")
    
if m>=33 and m<=100:
    print("pass in maths")
else:
    print("fail  in maths")
    
if e>33 and e<=100:
    print("pass in english")
else:
    print("fail  in english")
    
if s>=33 and m>=33 and e>=33 :
    print(" the student is pass")
else:
    print("the student is fail")
    
if s<=33 or m<=33 or e<=33 :
    print(" the student is fail")
else:
    print("the student is pass")
    


#Q3.a spam comment is definded as a text containing following keywords
'''"make a lot of money","buy now","subscribe this","click this"'''
    #write a program to detect these spams
#solution1
"not efficient "
text=input("Enter the key words to check spam text: ")
spam=["make a lot of money","buy now","subscribe this","click this"]
if text in spam:
    print("spam text")
else:
    print("not a spam text")
#solution2
if "make a lot of money" in text:
    spam=True
elif "buy now" in text:
    spam=True
elif "subscribe this" in text:
    spam=True
elif "click this" in text:
    spam=True
if spam:
    print("this text is spam")
else:
    print("this text is not spam")



#Q4.write a program to find whether a given username contains less then 10 character or not
usernme=input("enter username")
if len(usernme)<=10:
    print("the username contains less than 10 characters")
else:
    print("the username contains more than 10 characters")



#Q5.write a program which finds out whether given name is present in a list or not
name=input("Enter your name:")
a=["Rohit","shubbham","vikas","ashis","kuldeep","ganesh"]
if name in a:
    print(f"the Name {name} present in the list")
else:
    print(f"this Name {name}is new and not present in the list")


#Q6.write a program to calculate the grade of a student from his marks from the following scheme
marks=int(input("Enter the Marks:"))
if marks>90 and marks<=100:
    print("Ex")
elif marks>80 and marks<=90:
    print("A")
elif marks>70 and marks<=80:
    print("B")
elif marks>60 and marks<=70:
    print("C")
elif marks>50 and marks<=60:
    print("D")
elif marks>100 and marks<0:
    print("Invalid input")
else:
    print("f")



#Q7.write a program to find out whether a given post is talking about "rohit" or not
#solution1 -- complex
post=input("Enter the post:")
name=["rohit","Rohit","rOhit","roHit","rohIt","rohiT","ROhit","rOHit","roHIt","rohIT","RoHit","RohIt","RohiT","rOhIt","rOhiT","roHiT","RoHiT","ROHit","rOHIt","roHIT","ROHIt","rOHIT","RoHIT","ROhIT","ROHiT","ROHIt","ROHIT"]
if post in name:
      print("the post is talking about Rohit")
else:
    print("the post not talking about rohit")

#solution2--easy and logical
if 'rohit' in post.lower():
    print("The post is talking about Rohit")
else:
    print("The post not talking about post")
