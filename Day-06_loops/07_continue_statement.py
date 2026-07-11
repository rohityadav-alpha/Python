for i in range(10):
    if i == 5:
        continue  #--it skips the value of i=5 and control comes back to the loop
    print(i)
else:
    print("loop completed normally with skip of i=5")