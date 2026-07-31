
'''class students:
    college="gyannodya vidya madir"             #--------\
    country="india"                             #---------\ this are class attributes/variables
    subject=['maths','science','english','geography']#-----\

    def __init__(self,name,age,division,mark):   #constructor method
        self.name=name
        self.age=age
        self.division=division
        self.mark=mark
    
    def getStdInfo(self):                       #instance method
        print(f"name:{self.name} \nage:{self.age} \ndivision:{self.division} \nmark:{self.mark} \nsubjects:{self.subject} \ncollege:{self.college} \ncountry:{self.country} ")

s1=students("rohit",23,"A",95.67)  #these are instance attributes/variables
s1.getStdInfo()

s2=students("roshan",22,"B",78.9)  #these are instance attributes
s2.getStdInfo()
'''

#create student class that takes name & marks of 3 subjects as arguments in constructor then create a method to print the avgrage.

class student:

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @property
    def getAvgMarks(self):
        sum=0
        for val in self.marks:
            sum+=val
        return sum//3

s1=student("rohit",[98,97.5,78])
print(f"hello {s1.name} your avg mark is {s1.getAvgMarks}") 