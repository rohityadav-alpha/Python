class First:    
    country="india"

    def __init__(self,address): #constructor
        self.address=address
        

    def getAddress(self):
        print("**grandparent class**")
        print(f"the address is {self.address}")

class Second(First):

    def __init__(self,course,degree,address): #constructor with his parents variables
        super().__init__(address)   #grandparent class constructor call
        self.course=course
        self.degree=degree
        

    def getEducation(self):
        print("**parent class**")
        print(f"the course is {self.course} and the degree is {self.degree}")

class Third(Second):
    def __init__(self,name,age,classes,course,degree,address):  #constructor with his parents variables
        super().__init__(course,degree,address) #grandparent and parent class constructor call
        self.name=name
        self.age=age
        self.classes=classes
        

    def getStudentInfo(self):
        print("**child class**")
        print(f"name:{self.name}  age:{self.age}  classes:{self.classes}")

obj3=Third("ravi",23,"A","Python","Graduation","thane")
obj3.getStudentInfo()
obj3.getEducation()
obj3.getAddress()
print(obj3.country)

        

