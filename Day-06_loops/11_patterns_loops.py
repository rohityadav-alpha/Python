'''#Q1. write a program to print following pattern using loops
# *
# * * 
# * * *
# * * * *
num= int(input("Enter the number of rows: "))
for i in range(num):
    print(" * "*(i+1))



#Q2. write a program to print following pattern using loops
#     *
#   * * *
# * * * * *
num= int(input("Enter the number of rows: "))
for i in range(num):
   print(" "*(num-i-1),end="")
   for j in range(num):
        print("*"*(2*i+1),end="")
   print(" "*(num-i-1))

#Q3.write a program to print following pattern using loops
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
num= int(input("Enter the number of rows: "))
for i in range(num+1):
    for j in range(num+1):
        print(" * ",end="")
    print()


#Q4.write a program to print following pattern using loops
# * * *
# *   *
# * * *
#solution1
for i in range(3):
    for j in range(3):
        if j==1 and i==1:
            print("  ",end="")
        else:
            print("* ",end="")
    print()
#solution2
rows=int(input("enter the number ;"))
col=rows
for i in range(rows):
    for j in range(col):
        if i==0 or i==rows-1:
            print("* ",end="")
        elif j==0 or j==col-1:
            print("* ",end="")
        else:
            print("  ",end="")
    print()
'''
#    *    
#  *   *    
# *     *   
#*       *  
#* * * * *
num= int(input("Enter the number of rows: "))
for i in range(num):
    if i<1 or i==num-1 :
        print(" "*(num-i-1),end="")
        print("*"*(2*i+1),end="")
        print(" "*(num-i-1))
    else:
        print(" "*(num-i-1),end="")
        print("*",end="")
        print(" "*(2*i),end="") 
        print("* ",end="")
        print(" "*(num-i-1))


