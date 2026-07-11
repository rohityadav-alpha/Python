#Question 1 :  Take Name and Age. If age>=18 and name!='Rohit', print Eligible else No Eligible.
name=input("Enter the name :")
age=int(input("Enter the age :"))
if age>=18 and name.lower()!='rohit':
    print("Eligible")
else:
    print("not Eligible")
    
