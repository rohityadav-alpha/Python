class Student:
    college="gvm"
    def __init__(self,name):
        self.name=name

    def getName(self):
        print(self.name)

s1=Student("rohit")
s1.getName()
print(s1.college)
del s1.college    # del keyword use to delete class and instance atrributes 
del s1.name
s1.getName()
print(s1.college)

    