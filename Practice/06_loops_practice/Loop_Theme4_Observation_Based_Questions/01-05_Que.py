# 1.What will this loop print, and why does the counter behave unexpectedly?
for i in range(5):
    if i == 3:
        i = 10
    print(i)


#for loop takes next value from range() object not from current value of variable



#2. Find the bug in this loop that is supposed to print numbers 1 to 5 but produces incorrect output.
i = 1
while i <= 5:
    print(i)
    i = i + 1
    if i == 3: #befor this statement yhe loop is already sexecuted continue is a misleading statement it does not affect the while loop execution
        continue
# for loop
for i in range(1,6):
    print(i)
    if i==3:
        continue #befor this statement yhe loop is already sexecuted continue is a misleading statement it does not affect the while loop execution

