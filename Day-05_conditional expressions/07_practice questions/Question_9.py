#Question 9:Check whether a string is palindrome.
word=input("enter the word")
if word==word[::-1]:
    print(f"the word {word} is palindrome")
else:
    print(f"the word {word} is not palindrome")
