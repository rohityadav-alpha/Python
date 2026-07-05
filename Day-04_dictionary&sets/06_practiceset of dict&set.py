#Q1.write a program to create a dict of hindi words with values as their english translation. provide user with an option to look it up 
hindi_dict={
    "namaste":"hello",
    "swagat":"welcom",
    "wishram":"rest"
    }
print("namaste in english translation is",hindi_dict["namaste"],"\n")
'''print("options are",hindi_dict.keys())
lan=input("enter the language:")
print(f"the word {lan} in english is {hindi_dict[lan]}\n")'''


#Q2.write a program to input eight numbers from the user and display all the unique numbers(once)
'''n1=int(input("Enter number 1st:"))
n2=int(input("Enter number 2nd:"))
n3=int(input("Enter number 3rd:"))
n4=int(input("Enter number 4th:"))
n5=int(input("Enter number 5th:"))
n6=int(input("Enter number 6th:"))
n7=int(input("Enter number 7th:"))
n8=int(input("Enter number 8th:"))
#if you enter any number twice or more it print only one time 
set1={n1,n2,n3,n4,n5,n6,n7,n8}
print(type(set1))
print(set1)'''


#Q3.can we have a set with 18(int) and 18(str)
set2={18,"18"}
print(set2)
#yes

#Q4.what will be the length of following set s
s=set()
s.add(20)
s.add("20")
s.add(20.0) #is element 20.0 as same as 20 so it count as one 20 because set is a non repetable container and 
print(s)
print(len(s))


#Q5.s={} what is a type of s
s={}
print(s)
print(type(s)) #it returns <class'dict'>


#Q6.create an empty dict and allow frnds to add their fav language as value and their name as key
#solution1
dict1={}
print(dict1)
updated_dict={
    "rohit":"hindi",
    "shubham":"marathi",
    "ganya":"bangali",
    }
dict1.update(updated_dict)
print(dict1)
#solution2
'''frnd={}
a=input("enter the fav language of rohit:")
b=input("enter the fav language of shubham:")
c=input("enter the fav language of ganya:")
frnd['rohit']=a
frnd['shubham']=b
frnd['ganya']=c
print(frnd)'''


#Q7.if name of  2 frinds are same what will happen to the program in problem6?
#if the names of 2 frnds are same but the values are different then the last updated value is considered
dict2={}
print(dict2)
updated_dict2={
    "rohit":"hindi",
    "shubham":"marathi",
    "ganya":"bangali",
    "rohit":"tamil",
    "vikas":"bangali",
    "shubham":"marathi"
    }
dict2.update(updated_dict2)
print(dict2)


#Q8.if language of  2 frinds are same what will happen to the program in problem6?
#if the language of 2 frnds are same but the names are different then the last updated value is considered


#Q9.can you change the value inside alist which is contained in set S
#S={8,3,66,7,[1,3],"rohit"}
#print(S) --it return error , sets cannot contail list ,lists are mutable 
