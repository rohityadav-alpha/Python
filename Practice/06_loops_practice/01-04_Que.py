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


# 5. [Medium] Print a hollow pyramid (triangle) of height n.
def hollow_pyramid(n):
   for i in range(1,n+1):
      print("  "*(n-i),end="")
      for j in range(1,2*i):
         if j==1 or j==(2*i-1) or i==n:
            print("* ",end="")
         else:
            print("  ",end="")
      print()
         
hollow_pyramid(5)
# 5. [Medium] Print a hollow inverted pyramid (triangle) of height n.
def hollow_pyramid(n):
   for i in range(n-1,0,-1):
      print("  "*(n-i),end="")
      for j in range(1,2*i):
         if j==1 or j==(2*i-1) or i==n:
            print("* ",end="")
         else:
            print("  ",end="")
      print()
         
hollow_pyramid(5)
 

# 6. [Medium] Print a hollow diamond pattern of given size n.
# solution 1
def hollow_Diamond(n):
   for i in range(3,n+1):
      print("  "*(n-i),end="")
      for j in range(1,2*i):
         if i==n-2 or j==1 or j==(2*i-1):
            print("* ",end="")
         else:
            print("  ",end="")
      print() 
   for i in range(n-1,0,-1):
      print("  "*(n-i),end="")
      for j in range(1,2*i):
         if j==1 or j==(2*i-1) or i==n:
            print("* ",end="")
         else:
            print("  ",end="")
      print()  
hollow_Diamond(5)
# solution 2
def HollowDiamond(n):
   def half(N):
      for i in N:
         print("  "*(n-i),end="")
         for j in range(2*i):
            if j==1 or j==(2*i-1):
               print("* ",end="")
            else:
               print("  ",end="")
         print()
   half(range(3,n+1))
   half(range(n-1,0,-1))
HollowDiamond(5)


# 7. [Medium] Print Pascal's Triangle up to n rows.
def pascals_triangle(n):
   triangle = []
   for i in range(n):
      row = [1] * (i + 1)
      for j in range(1, i):
         row[j] = triangle[i-1][j-1] + triangle[i-1][j]
      triangle.append(row)
      print(row)
   return triangle

pascals_triangle(5)
# solution 2
def pascals_triangle(n):
    triangle = []
    for row in range(n):
        # Create an empty list for the current row and append 1
        current_row = [1]
        if row > 0:
            last_row = triangle[row - 1]
            for i in range(1, row):
                value = last_row[i - 1] + last_row[i]
                current_row.append(value) 
            # Append the last 1 to the current row
            current_row.append(1)
        # Add the current row to the triangle
        triangle.append(current_row)
    # Print Pascal's Triangle
    for row in triangle:
        print(' '.join(map(str, row)).center(n * 3))
# Example usage: Print Pascal's Triangle up to 5 rows
pascals_triangle(5)
