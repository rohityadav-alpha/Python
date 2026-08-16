# solution 1
def diamond(n):
   for i in range(round((n/100)*60),n+1):
      print("* "*(n-i),end="")
      for j in range(1,i*2):
         if j==1 or j==(i*2-1) or i==round((n/100)*60) or i==n :
            print("# ",end="")
         else:
            print("* ",end="")
      print("* "*(n-i),end="")
      print()
   for i in range(n-1,0,-1):
      print("* "*(n-i),end="")
      for j in range(2*i-1,0,-1):
         if j==1 or j==(i*2-1) or i==n:
            print("# ",end="")
         else:
            print("* ",end="")
      print("* "*(n-i),end="")
      print()
diamond(5)