#Question 7:English: Login validation using username and password dictionary.
user_pass={
    "username":"@rohit47",
    "password":"rohit47"}
username=input("Enter username:")
password=input("Enter password")
if username in user_pass["username"]  and password in user_pass["password"]:
    print("valid user")
else:
    print("invalid user")

