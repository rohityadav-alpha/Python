#Q1.write a program to store seven fruits in a list entered by the users
'''fruit1=input("enter 1st fruit name:")
fruit2=input("enter 2nd fruit name:")
fruit3=input("enter 3rd fruit name:")
fruit4=input("enter 4th fruit name:")
fruit5=input("enter 5th fruit name:")
list1=[fruit1,fruit2,fruit3,fruit4,fruit5]
print(list1)'''


#Q2.write a program to accept marks of 6 students and display them in a sorted manner

'''mark1=int(input("enter the marks1:"))
mark2=int(input("enter the marks2:"))
mark3=int(input("enter the marks3:"))
mark4=int(input("enter the marks4:"))
mark5=int(input("enter the marks5:"))
mark6=int(input("enter the marks6:"))
list2=[mark1,mark2,mark3,mark4,mark5,mark6]
list2.sort()
print(list2)'''


#Q3.check that a tuple cannot be change in python
#this returns error
t=(1,4,5)
#t(1)=6 
#t[0]=3
print(t)


#Write a program to sum a list with 4 numbers
list3=[6,3,9,2]
print(sum(list3)) #1st method
print(list3[0]+list3[1]+list3[2]+list3[3]) #2nd method this is not relevent for larger list

#wrrrite a program to count the number zero in the following tuples
a=(7,0,8,0,0,9)
zerocount=a.count(0)
print(a.count(0)) #1st method
print(zerocount) #2nd mrthod


