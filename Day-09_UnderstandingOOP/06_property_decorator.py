class employee:
    name="rohit"
    age=23
    salary=5500
    insentive=600
    company="google"

    # def totalSalary(cls):  #if we dont use @property then we have to call method 
    #      cls.totalsalary=cls.salary+cls.insentive
    #      return cls.totalsalary

    @property        #@property is use to return function/method into form of  property
    def totalSalary(cls):
         cls.totalsalary=cls.salary+cls.insentive
         return cls.totalsalary
        

obj=employee()
print(obj.salary)
# print(obj.totalSalary()) #if we are not using @property we have to call the method than print it 
print(obj.totalSalary)  #it print method in the form of property