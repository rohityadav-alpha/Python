n=10
for i in range(n):
    print("  "*(n-i),end="")
    print("* "*(2*i-1),end="")
    print(" "*(n-i))
print()