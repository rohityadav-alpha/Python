#Question 5:You are building a mobile recharge checker. A user is considered active only when the entered plan type is
#daily. Take Mobile Number and Plan Type as input. Print Plan Active if the plan matches, otherwise print
#Plan Not Supported.
name=input("Enter your Name")
plan=input("Enter tour Plan")
if 'daily' in plan.lower():
    print("Plan Active")
else:
    print("Plan Not Supported.")
