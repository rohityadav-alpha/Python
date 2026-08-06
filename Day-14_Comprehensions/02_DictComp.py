# dictionary of containing the pair of number:numbersquare from 1-10
square={i:i**2 for i in range(1,11)}
print(square)

# dictionary containg name age pair
name=['rohit','rahul','sanjay']
age=[20,21,22]
dict1={name:age for name,age in zip(name,age)} #--zip() function is used to combine two lists into a dictionary
print(dict1)

#Length mapping
words = ["apple", "banana", "cherry"]
length={i:len(i) for i in words} #--len() function is used to get the length of the word
print(length)

#Character frequency in a string
word='hello'
freq={i:word.count(i) for i in word} # .count() function is used to count the frequency of each character in the string
print(freq)

# Nested dictionary (student → subject → marks)




