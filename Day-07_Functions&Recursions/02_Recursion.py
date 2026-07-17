num=int(input("enter the number:"))

#write a function to calculate factorial
#using loop
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
print(factorial(num))
#using recursive formula
def fact_rec(n1):
    if n1==1 or n1==0:
        return 1
    else:
        return n1*factorial(n1-1)
print(fact_rec(num))
    


#write a function to print first n natural number
#using loop
def fibonacci(n2):
    fi=0
    for i in range(n2+1):
        fi=fi+i
    return fi
print(fibonacci(num))
#using recursive formulas
def fibo_rec(n3):
    if n3==0:
        return 0
    else:
        return n3+fibo_rec(n3-1)
print(fibo_rec(num))


#write a function to print pattern of a number 
def pattern(p):
   for i in range(p):
      print("*"*(p-i))
pattern(num)
        

#write a program to print multiplication of a table

def multable(n4):
   for i in range(10+1):
       print(f"{n4} X {i}= {n4*i}")
   return n4
multable(num)
    









