#check the person is young elder or scenior citizen (using relational(>=,<=,<,>) & logical(and,or,not) operator)

#and 
age1=int(input("Enter the age of person:"))
if age1<18:
    print("the person is child")
elif age1>=18 and age1<30:
    print("the person is young")
elif age1>=30 and age1<=50:
    print("the person is elder")
else:
    print("the person is senior citizen")

#check the condition and and allow childers and olders to get medical support first
#or
age2=int(input("Enter age of the person:"))
if age2<18 or age2>60:
    print("he/she can get the medical support")
else:
    print("go after childers/oldres")


#check the person is eligible for vote or not 
#not
age3=int(input("Enter age of the person:"))
if not age3<18:
    print("he/she can vote")
else:
    print("not eligible for vote")
