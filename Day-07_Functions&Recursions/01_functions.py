#Function
#A function is a group of statements performing a specific task
#The part containg the exact set of instructions which are executed during the functions call
#Ex. I created a function that calculates percentage of a list that can calculate 4 elements of list

def percentage(marks):
    return ((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

l=[45,67,94,74]
print(percentage(l))

l1=[83,97,88,99]
print(percentage(l1))


#write a program to greet user with good morning
name=input("enter your name ")
def greet(nam="unknown"):
    return ("good morning "+nam)

print(greet(name))
