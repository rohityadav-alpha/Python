#It’s a convention in Python that says “this is for internal use, don’t touch directly outside class.”
# Accessible inside the class.
# Accessible in subclasses (child classes).
# Technically accessible outside class also, but discouraged.

class Acc_no:
    def __init__(self,acc,pin):
        self.acc=acc
        self._pin=pin

class Pin(Acc_no):
    def getInfo(self):
        print(self.acc,self._pin)
        

a1=Pin(23415,9876)
print(a1.acc)
print(a1._pin) #it works but not recommended
a1.getInfo()
a2=Acc_no(785364,6475)
print(a2._pin)

