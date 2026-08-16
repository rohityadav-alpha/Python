# 1. [Easy] Print a right-angled triangle of stars of height n.
def rightAngle(n):
# solution 1 -- nested loop
   for i in range(n):   
    for j in range(i):
        print('*',end="")
    print("")
# solution 2 -- single loop
   for i in range(n):   
    print('*'*i)
rightAngle(6)
   
# 2. [Easy] Print an inverted right-angled triangle of stars.
def invertTriangle(n):
# solution 1 --nested loop
   for i in range(n):   
    for j in range(n-i):
        print('*',end="")
    print("")
    # solution 2--single loop
   for i in range(n):
       print('*'*(n-i))
invertTriangle(5)


# 3. [Easy] Print a pyramid (centered triangle) of stars of height n.
def piramid(n):
   for i in range(1,n):
      print(" "*(n-i) , end="")
      print('*'*(2*i-1),end="")
      print(" "*(n-i))
piramid(5)


# 4. [Medium] Print a hollow square of size n using stars.
def squareshape(n):
    for i in range(1,n):
        for j in range(1,n):
            if i==1 or j==1:
               print('* ',end="")
            elif i==(n-1) or j==(n-1):
               print('* ',end="")
            else:
               print("  ",end="") 
        print("")
squareshape(5)
