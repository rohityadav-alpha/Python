class student:
    def __init__(self,name,age,course): #constructor
        self.name=name
        self.age=age
        self.course=course
        print("this is parent class")

    def getInfo(self):  #intence method
        print(f"student information name:{self.name} and age:{self.age}")

class courses(student):
    def getCourse(self,):
        print("this is child class")
        print(f"course of the student{self.name} is {self.course}")

#    def getInfo(self):    #method overriding
            #print(f"student information name:{self.name} , age:{self.age} and couses: {self.course}")



obj=courses("rohit",23,"basic python")
obj.getInfo() #geting information(data,values) from child(courses) class 
obj.getCourse() 