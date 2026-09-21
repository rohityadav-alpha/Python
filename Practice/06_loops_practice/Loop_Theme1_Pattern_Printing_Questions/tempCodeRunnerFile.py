def zigZag(n):
   N=n*3
   odd1=[i for i in range(1,N,4)]
   even=[i for i in range(1,N) if i%2==0]
   odd2=[i for i in range(3,N,4)]
   for i in range(1,n+1):
      for j in range(N):
         if i%2==0 and j in even:
            print("* ",end="")
         elif i and j in odd1:
            print("* ",end="")
         elif i and j in odd2:
            print("* ",end="")
         else:
            print("  ",end="")
      print()
zigZag(3)