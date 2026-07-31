'''
#Q1.Create a class programmer for storing information of two programmers working at microsoft
class Programmer:
    company="microsoft"
        
    def __init__(self,name,age,salary):
        print("programmer class is created")
        self.name=name
        self.age=age
        self.salary=salary
    
    def getDetail(self):
        print(f"Name={self.name}, age={self.age}, salary={self.salary} , company={self.company}")

rohit=Programmer("rohit",23,1000,)
vikas=Programmer("vikas",22,10000,)
rohit.getDetail()
vikas.getDetail()

#Q2.write class calculator capable os finding square, cube , squareroot of a nummber
num=int(input("enter the number:"))
class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"Square of a number {num} is {num*num}")

    def squareRoot(self):
        print(f"Square Root of a number {num} is {round(num**(1/2))}")

    def cube(self):
        print(f"cube of a number {num} is {num*num*num} ")

    def cubeRoot(self):
        print(f"cube of a number {num} is {round(num**(1/3))} ")

Number=Calculator(num)
Number.square()
Number.squareRoot()
Number.cube()
Number.cubeRoot()


#Q3.create a class with a class attributes a ; create an object from it and directly using object.a=0 dose this changes a class attributes?
class Example:
    a=5000

obj=Example()
Example.a=0      #it can be change a class attribute value
obj.a=0          #it create a intance attribues seperatly does not effects or change class attributes value
print(obj.a)     #it print object.a intance attribute
print(Example.a) #it prints class attribute


#Add a static method in program in problem 2 to greet the user with hello
num=int(input("enter the number:"))
class Calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"Square of a number {num} is {num*num}")

    def squareRoot(self):
        print(f"Square Root of a number {num} is {round(num**(1/2))}")

    def cube(self):
        print(f"cube of a number {num} is {num*num*num} ")

    def cubeRoot(self):
        print(f"cube of a number {num} is {round(num**(1/3))} ")
    
    @staticmethod
    def greet():
        print(f"Hello")

Number=Calculator(num)
Number.greet()
Number.square()
Number.squareRoot()
Number.cube()
Number.cubeRoot()


#Q5.write a class train which has methods to book a ticket get train info(number of seats) and get fare information of train running under indian railways
class Train:
    def __init__(self, name , fare , seats):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getInfoTrain(self):
        print(f"the name of the train is {self.name}")
        print(f"the price of the train is Rs. {self.fare}")
    
    def getSeats(self):
        print(f"the number of seats available in train is {self.seats}")
    
    def bookTicket(self):
        if self.seats>0:
            print(f"your ticket is booked :seat no. {self.seats}B")
            self.seats=self.seats-1
        else:
            print("train is full")
        

superfast= Train("gomti exp: 12876", 500, 2)
superfast.getInfoTrain()

superfast.bookTicket()
superfast.bookTicket()
superfast.bookTicket()

superfast.getSeats()
'''
'''
#we can use slf or any other parameter on the place of self in class methodas
#because self is a parameter

class person:
    def __init__(slf,name):
        slf.name=name
rohit=person("Rohit")
print(rohit.name)
'''

#Write a Python program program for basic banking system -- create account class with 2 attributes balance,accountno. create method for debit , credit & printing the balance
class Account:

    def __init__(self,name,bal,acc):
        self.balance=bal
        self.AccountNo=acc
        self.name=name

    def debit(self,amt):
        self.balance-=amt
        print(f"{self.name} Rs.{amt} is debited from your account no.{self.AccountNo}")
        print(f"availale balance Rs.{self.getBalance()}")
        
    def credit(self,amt):
        self.balance+=amt
        print(f"{self.name} Rs.{amt} is credited in your account no.{self.AccountNo}")
        print(f"availale balance Rs.{self.getBalance()}")

    def getBalance(self):
        return self.balance

a1=Account("rohit",20000,256175)
a1.debit(700)
a1.credit(1300)
