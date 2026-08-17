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


#3. What is the off-by-one error in this code meant to print the last 3 elements of a list, and how do you fix it?
arr = [10, 20, 30, 40, 50]
for i in range(len(arr) - 3, len(arr)): # this will be goes under negetive index if the length of the list is less then 3 
    print(arr[i])
# solution 
arr = [10, 20]
for i in range(max(0,len(arr) - 3),len(arr)): # to avoide the negetive indexing use max(0,len(arr)-3) it set max value upto zero it prevent the startig value becomes zero
    print(arr[i])
