# generator function is a special type of function that produce values on the fly
# normal function uses return keyword to produce values and stop execution
# generator function uses yield keyword to produce values one at a time and puses the state of the function until the next value is requested.



# normal function
def NUM(n):
    return n
obj=NUM(5)
print(obj)
#generator function
def gen():
    yield 1
    yield 2
    yield 3
g=gen()
print(g)

# create a generator function that takes a string as input and yields each character of the string one at a time.
name="rohit"
def gen(n):
    for i in n:
        yield i
g=gen(name)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print("\n")
#generator function with for loop
for i in gen(name):
    print(i)