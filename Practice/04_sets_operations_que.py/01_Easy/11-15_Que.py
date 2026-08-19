# 11. Convert a string into a set of unique characters.
s1="rohit roshan ravi"
def convert(s):
    return set(s)
print(convert(s1))

# 12. Remove an element from a set safely.
s2={2,4,7,9,1,6,5,8,3}
# solution 1 -- using remove() method
def removeEl(s,e):
    s.remove(e)
    return s
print(removeEl(s2,2))
# solution 2 -- using discard() method
def rem(s,e):
    s.discard(e)
    return s
print(rem(s2,6))




# 13. Count how many unique words are present in a sentence.
sentence='''dear sir
     my name is rohit yadav
    i m writing this regard
    my 5 days hollidays
              thanks sirdear sir
                   my name is rohit yadav
                  i m writing this regard
                  my 5 days hollidays
                            thanks sirdear sir
                                 my name is rohit yadav
                                i m writing this regard
                                my 5 days hollidays
                                          thanks sir'''
print(sentence.split())
print(set(sentence.split()))
def countunique(s):
    return len(set(s.split()))
print(countunique(sentence))



# 14. Check if two sets are equal.
s3={1,2,3,4,5}
s4={5,4,3,2,1}
def checkEqual(set1,set2):
    return set1==set2
print(checkEqual(s3,s4))



# 15. Create a frozen set from a list and explain why it is useful.
list1=[1,2,3,4,5]
fs=frozenset(list1)
print(fs)
# A frozen set is an immutable version of a set. Once created, its elements cannot be changed, added, or removed. This makes it useful for creating a set that should not be modified after creation, ensuring data integrity.