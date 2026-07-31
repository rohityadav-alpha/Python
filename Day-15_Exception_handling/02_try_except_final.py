try :
    a=int(input("enter the number: "))
    b=9/a
    print(b)
except ZeroDivisionError :
    print(f"the number is not divisibale by {a}")
except Exception as e:
    print("the type of the error is:",e)
finally :
    print("this will execute always")