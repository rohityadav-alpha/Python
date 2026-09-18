# 16. [Tricky] Print a butterfly pattern (two triangles joined at the base, mirrored horizontally).

def butterfly(n):
      def but(rng):
         for i in rng:
            print("* "*(i),end="")
            for j in range(i+1,(n*2)):
               if j==i or j==((n*2)-i) or j>=((n*2)-i):
                  print("* ",end="")
               else:
                  print("  ",end="")
            print()
      but(range(1,n+1))
      but(range(n,0,-1))
butterfly(5)