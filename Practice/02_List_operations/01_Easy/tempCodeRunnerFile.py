# 15. Swap the First and Last Element of a List
numbers = [1, 2, 3, 4, 5, 6]
def swap(l):
    l[0],l[-1]=l[-1],l[0]
    return l
print(swap(numbers))