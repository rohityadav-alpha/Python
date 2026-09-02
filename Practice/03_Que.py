#Write a function to count the number of vowels in a string.
def Vovel(st:str)->int:
    
    num=0
    i=1
    for i in len(st):
        if 'a' in st:
            num+=i
        if 'e' in st:
            num+=i
        if 'i' in st:
            num+=i
        if 'o' in st:
            num+=i
        if 'u' in st:
            num+=i
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