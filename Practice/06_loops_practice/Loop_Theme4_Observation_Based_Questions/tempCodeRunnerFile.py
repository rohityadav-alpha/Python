#5. This loop is meant to find the first negative number in a list, but it has a flag-based logic bug. Identify and fix it.
list1=[1,6,2,-8,5,-9,4,3,7]
def find_first_negative(arr):
    found = False
    result = 0
    for num in arr:
        if num < 0:
            found = True
        if found:
            result = num
            break
    return result
print(find_first_negative(list1))