#dictionary methods

dict1={"name":"rohit yadav",
       "age":[23],
       "marks":{"maths":[69],
                "science":[89],
                "physics":[75]},
       "is_student":"Yes",
       "numbers":[3,8,5,4]}
print(dict1)
print(dict1["name"])    #returns error if the key is not present in dictionary--interview que
print(dict1.get("name"))#returns none if the key is not present in dictionary--interview que
print(dict1.keys())      #it returns all keys from the dictionary
print(dict1.values())    #it returns all the value of the keys from dictionary
print(dict1.items())    #it returns dictionary like a tuple form



