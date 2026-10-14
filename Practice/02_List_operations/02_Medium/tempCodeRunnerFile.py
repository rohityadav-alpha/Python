# 2. Find the missing number in a list of 1 to N.
listn=[n for n in range(1,11) if n!=4 ]
last=listn[-1]
total=last*(last+1)/2
SUM=sum(listn)
result=total-SUM
print(result)