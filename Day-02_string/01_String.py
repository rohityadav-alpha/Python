#string

#single line string
letter=" hello!,rohit yadav"
letter1='hello!, ravi rathod'
print(letter)
print(letter1)

#multiline string
letter2='''
dear! rohit yadav
    your selected for nit trichi
    thanks!
             '''
print(letter2)

letter3="""
dear! rohit yadav
    your selected for nit trichi
    thanks!
"""
print(letter3)


#if the string values contains single cout in it so we use " court to write string
letter4="this is a rohit's book"
print(letter4)

#if the string values contains double cout in it so we use ' court to write string
letter5='the name "rohit" is a popular name '
print(letter5)

letter6='''
  dear sir
     my name is rohit yadav
    i m writing this regard
    my 5 days hollidays
              thanks sir
'''
print(letter6)
print(f"Datatype of the letters value is {type(letter6)}")
print(f"length of the letter is : {len(letter6)}")

name="rohitt"
print(name.count("t"))