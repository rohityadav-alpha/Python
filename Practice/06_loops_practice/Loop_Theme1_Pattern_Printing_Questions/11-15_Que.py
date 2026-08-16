#06_loops_practice\Loop_Theme1_Pattern_Printing_Questions\11-15_Que.py
# 11. [Medium] Print an alternating 1 and 0 pyramid pattern.
def patter_piramid(n):
   for i in range(n+1):
      print("  "*(n-i),end="")
      for j in range(1,i*2):
         if j%2==0:
            print("1 ",end="")
         else:
            print("0 ",end="")
      print()
patter_piramid(5)
# solution 2
def alt_pyramid(n):
   for i in range(1,n+1):
      print("  "*(n-i),end="")
      bit=i%2
      for j in range(2*i-1):
         print(bit ,end=" ")
         bit=1-bit
      print()
alt_pyramid(5)


# 12. [Hard] Print an alphabet pyramid where each row contains letters up to the row's corresponding letter (A, A B, A B C...).
# solution 1 -- normal logic
def abc(n):
   for i in range(n+1):
      for j in range(i):
         print(chr(65+j),end=" ")
      print()
abc(5)
# solution 2 --comprehension logic
def alphabet_pyramid(n):
   for i in range(n):
      row = [chr(65+j) for j in range(i+1)]
      print(" ".join(row))
alphabet_pyramid(5)



# 13. [Hard] Print a mirrored (right-aligned) number triangle where numbers increase from right to left.
# soution 1 -- normal logic
def mir(n):
   for i in range(1,n+1):
      print(" "*(n-i),end="")
      for j in range(i,0,-1):
         print(j,end="")
      print()
mir(5)
# solution 2 --comprehension logic
def mirrored_triangle(n):
   for i in range(1, n+1):
      spaces = " " * (n - i)
      nums = "".join(str(x) for x in range(i, 0, -1))
      print(spaces + nums)
mirrored_triangle(5)


# 14. [Hard] Print a diamond pattern using alternating characters based on row parity (odd rows use '*', even rows use '#').
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
# output:
#   * * # # # # # * * 
#   * # * * * * * # * 
#   # # # # # # # # # 
#   * # * * * * * # * 
#   * * # * * * # * * 
#   * * * # * # * * * 
#   * * * * # * * * *
# solution 2
def parity_diamond(n):
   def half(rng):
      for i in rng:
         ch = "*" if i % 2 != 0 else "#"
         print(" " * (n-i) + ch * (2*i-1))
   half(range(1, n+1))
   half(range(n-1, 0, -1))
parity_diamond(5)
# output 
#     *
#    ###
#   *****
#  #######
# *********
#  #######
#   *****
#    ###
#     *


# 15. [Hard] Print a spiral-filled square matrix pattern with numbers 1 to n*n.