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