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

def duplicate(s):
    list1=s.split()
    s1=set(list1)
    nlist=[]
    for el in list1:
        if el not in s1:
            pass
        else:
            nlist.append(el)
    return set(nlist)
print(duplicate(sentence))
