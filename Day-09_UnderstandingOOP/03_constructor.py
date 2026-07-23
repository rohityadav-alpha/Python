#constructor execute as soon as the object is created
class Employee:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"emp_name={name} and emp_age={age}") #see the difference construction execution

    def getDetail(self):
        print(f"emp_name={self.name} and emp_age={self.age}") #here method

obj=Employee("rohit",23)
obj.getDetail()