#write a python program to reverce number 
num=int(input("enter the number"))
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10
print(rev)

num=100
for i in range(num):
    if i%2==0:
        print(i)