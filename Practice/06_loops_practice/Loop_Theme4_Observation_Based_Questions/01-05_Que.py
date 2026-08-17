# 1.What will this loop print, and why does the counter behave unexpectedly?
for i in range(5):
    if i == 3:
        i = 10
    print(i)