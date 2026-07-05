#properties of dictionary
'''
it is unordered
it is mutable
it is indexed
it cannot contain dublicate value
'''

#dictionary syntax
dict_name={
    "key":"value",
    "inner_dict":{"key1":"value"} #nested dictionary 
    }



dict1={"name":"rohit yadav",
       "age":[23],
       "marks":{"maths":[69],
                "science":[89],
                "physics":[75]},
       "is_student":"Yes"}
print(dict1)
print(dict1['name'])
print(dict1['marks'])
print(dict1['marks']['maths'])
