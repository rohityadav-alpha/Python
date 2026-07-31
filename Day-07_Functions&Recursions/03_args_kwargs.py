# *args stores values or takes values in tuples as a positional argument input
def Addition(*args):
    Sum=0
    for val in args:
        Sum+=val
    print(Sum)

Addition(2,6,4,9)


# **kwargs stores values in list in the form key Value pair providing input keyword arguments
def Dict(**kwargs):
    print(kwargs)
    for key,val in kwargs.items():
        print(f"{key} = {val}")

Dict(name="rohit", marks=58.7, age=23 )