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
def pascal_triangle(n):
  triangle =[]
  for i in range(n):
     print(" "*(n-i),end="")
     row=[1]*(i+1)
     for j in range(1,i):
        row[j]=triangle[i-1][j-1]+triangle[i-1][j]
     triangle.append(row)
     print(row)
pascal_triangle(4)


# 8. [Medium] Print a number pattern where each row repeats its row number (e.g., row 3 prints 3 3 3).
def pat(n):  
   for i in range(n):
      for j in range(i):
         print(i,end="")
      print()
pat(5)


# 9. [Medium] Print a floyd's triangle (continuously increasing numbers row-wise).
def floyds_triangle(n):
   num=1
   for i in range(1, n+1):
      row = []
      for j in range(i):
         row.append(str(num))
         num += 1
      print(" ".join(row))
floyds_triangle(5)