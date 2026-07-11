#Question 3:You are creating an ATM login screen. The ATM should allow access only when the entered PIN matches 4321.
#Take PIN as input. If the PIN is correct, print Access Granted; otherwise print Invalid PIN.
pin=int(input("Enter the 4 digit ATM Pin:"))
ATM_PIN=4321
if pin==ATM_PIN:
    print("Access Granted")
else:
    print("Invalid PIN")
