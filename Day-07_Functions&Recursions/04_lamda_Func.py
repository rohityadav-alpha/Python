#single argument
sqrt=lambda n : n*n
print(sqrt(3))

# multiple arguments
Add = lambda a,b: a+b
print(Add(3,5))

# percentage using lamda function
percentage=lambda marks:((marks[0]+marks[1]+marks[2]+marks[3])/400)*100

l=[45,67,94,74]
print(percentage(l))

l1=[83,97,88,99]
print(percentage(l1))