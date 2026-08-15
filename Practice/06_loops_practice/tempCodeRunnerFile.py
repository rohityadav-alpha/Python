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