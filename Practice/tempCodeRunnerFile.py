#Find the missing number from list 
def Miss(l):
    l.sort()
    n=l[-1]
    total=n*(n+1)/2
    s=sum(l)
    return total-s
print(Miss([2,4,0,1,6,5]))