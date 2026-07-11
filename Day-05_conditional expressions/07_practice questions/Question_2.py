#Question 2:Take a username. If length>8 and '@' exists, print Strong Username else Weak Username.
username=input("enter usnername :")
if len(username)>8 and '@' in username:
    print("strong password")
else:
    print("week password")

if len(username)<8:
    print("usnername must be more than 8 characters")

if '@' not in username:
    print("the username must be contain '@'")
