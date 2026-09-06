#Write a function to count the number of vowels in a string.
def Vovel(st:str)->int:
    list1=["a","e","o","u","i"]
    num=0
    i=1
    for i in list1:
        if i in st:
            num+=1
    return num
print(Vovel("rohit"))


# gst calculator
amount=int(input("Enter the base amount: "))
gst=int(input("Enter the gst percent just type the number: "))
class GSTcalculator:
    def amountWithGst(self,amt,gst):
        self.amt=amt
        self.gst=gst
        return amt+(amt*(gst/100))
    def amountWithNoGst(self,amt,gst):
        return amt-(amt*(gst/100))
GST=GSTcalculator()
print(GST.amountWithGst(amount,gst))
print(GST.amountWithNoGst(amount,gst))


# FizzBuzz problem 

# solution 2 without %modulo operator
def fizzBuzz(num):
    list3=[]
    list5=[]
    newlist=[]
    for i in range(1,num+1):
        for j in range(1,num+1):
            if i==5*j:
                list5.append(i)
            if i==3*j:
                list3.append(i)
    for i in range(1,num+1):
        if i in list3:
            newlist.append("Fizz")
        elif i in list5:
            newlist.append("Buss")
        elif i in list3 and i in list5:
            newlist.append("FizzBuss")
        else:
            newlist.append(i)
    return newlist
print(fizzBuzz(15))
