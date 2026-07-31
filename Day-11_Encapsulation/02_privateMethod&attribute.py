'''
#private attributes & methods are ment to be used only within the class and are not accessible from outside the class 
# Accessible only inside the class.
# Not directly accessible outside class or in subclass.
# Must use getter/setter methods to access.

class Account:
    country="india"
    __add="Indiranagar"   #private attribute

    def __init__(self,acc,pin):
        self.acc=acc
        self.__pin=pin

    def __Pass(self):   # this is a private method
        self.__pin

    def getPass(self):
        print(self.__pin)   #we can get private atrributes by creating method in the same class 

a1=Account(1342547,4356)
a1.getPass()                #this return pin because the getPass method is inside the same class and getPass is not a private method
print(a1.__pin)             #this return error because we cannot acces private attribute directly
print(a1.__Pass())          #this is also  return error because its a private method
'''

class Acc_no:
    def __init__(self,acc,pin):
        self.acc=acc
        self.__pin=pin

    def getInfo(self):
            print(self.acc,self.__pin)

class Pin(Acc_no):
    def getInfo(self):
        print(self.acc,self.__pin)
        

a1=Pin(23415,9876)
print(a1.acc)
# print(a1.__pin) ##it does not works because it is not accessible outside the class and in subclass
# a1.getInfo()  it doesnot work because the method is in subclass 
a2=Acc_no(785364,6475)
a2.getInfo() #this works because this method is inside the same class 
# print(a2._pin) #it does not work 