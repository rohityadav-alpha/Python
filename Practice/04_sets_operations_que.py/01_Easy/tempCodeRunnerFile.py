# 12. Remove an element from a set safely.
s2={2,4,7,9,1,6,5,8,3}
# solution 2 -- using discard() method
def rem(s,e):
    s.discard(e)
    return s
print(rem(s2,6))
# solution 1 -- using remove() method
def removeEl(s,e):
    s.remove(e)
    return s
print(removeEl(s2,2))
