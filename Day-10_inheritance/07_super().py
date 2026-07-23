class Employee:

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def Company(self,company):
        self.company=company

class Details(Employee):

    def __init__(self,name,salary,company,add):
        super().__init__(name,salary)   #parent class constructor call
        super().Company(company)        #paraent class instance method call
        self.add=add

    def getDetail(self):
        print(f"{self.name} , {self.salary} , {self.company} , {self.add}")

obj=Details("rohit",50000,'google',"Thane")
obj.getDetail()