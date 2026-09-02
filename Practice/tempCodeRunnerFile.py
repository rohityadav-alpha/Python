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