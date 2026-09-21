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


# 17. [Tricky] Print a zig-zag wave pattern of a character across fixed rows (like a sine wave using loops).
# solution 1
def zigZag(n):
   for i in range(n+1):
      for j in range(n*3):
         if i%2!=0 and j%2!=0:
            print("* ",end="")
         elif i%2==0 and j%2==0:
            print("* ",end="")
         else:
            print("  ",end="")
      print()
zigZag(3)
# solution 2
def zigzag_wave(rows, cols, ch="*"):
   grid = [[" "]*cols for _ in range(rows)]
   row, direction = 0, 1
   for col in range(cols):
      grid[row][col] = ch
      if row == 0:
         direction = 1
      elif row == rows-1:
         direction = -1
      row += direction
   for r in grid:
      print("".join(r))
zigzag_wave(4, 12)
# solution3
def zigZag(n):
   N=n*3
   odd1=[i for i in range(1,N,4)]
   even=[i for i in range(1,N) if i%2==0]
   odd2=[i for i in range(3,N,4)]
   for i in range(1,n+1):
      for j in range(N):
         if i%2==0 and j in even:
            print("* ",end="")
         elif i in odd1 and j in odd1:
            print("* ",end="")
         elif i and j in odd2:
            print("* ",end="")
         else:
            print("  ",end="")
      print()
zigZag(3)
