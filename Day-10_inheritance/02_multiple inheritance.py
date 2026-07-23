class Games:
    sports="cricket"
    team="indian"
    def __init__(self):  #constructor
            print("this is a parent1")

class person:
    name="rohit"
    age=23
    def __init__(self):  #constructor
        print("this is a parent2")

class participated(Games,person):
    def __init__(self):   #constructor
        print(f"this is a child class")

obj=participated() #i can access both parents from using child object 
print(f"person details  name:{obj.name} age:{obj.age} sports:{obj.sports} team:{obj.team}")

#print class
print(Games())  
print(person())