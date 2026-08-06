#write a python program to display a user entered name
#followed by good afternoon using input() function
'''
name=input("Enter your name:")
print("Good afternoon",name)
print("Good afternoon"+name)
'''


#write a python program to fill in a letter template
'''
#solution1
name=input("Enter your name:")
date=(input("Enter date :"))
letter= f"Dear {name} you are selected! on {date}"
print(letter)
'''
#write a python program to fill in a letter template
#solution2 using string function called replace function 
"""
letter= '''dear <name>
you are selected1
Date:<date>'''

name=input("Enter your name:")
date=(input("Enter date :"))
letter=letter.replace("<name>",name)
letter=letter.replace("<date>",date)
print(letter)
"""

#write a python program
#find double space in string
'''sentence="Rohit yadav is a  BTech student"
sentence=sentence.find("  ")
print(sentence)'''
#replace double space with single space
'''sentence=sentence.replace("  "," ")
print(sentence)'''


#write a py program to formate the following letter using escape sequence characters
#letter ="dear rohit, you are a good person. thanks!"

letter ="dear rohit, you are a good person. thanks!"
formate_letter= "dear rohit,\n\t you are a good person.\n thanks!"
print(letter)
print(formate_letter)




