#getters method is noyhing but a mehod named with @property decorator

class employee:
    name="rohit"
    age=23
    salary=5500
    insentive=600
    company="google"

    @property
    def totalSalary(self):  
        return self.salary+self.insentive
     

    @totalSalary.setter       #@name.setter is use to set values in defined variable function/method into form of  property
    def totalSalary(self,num):
         self.insentive=num-self.salary
        

obj=employee()
print(obj.salary)
print(obj.insentive)
print(obj.totalSalary)
print('**************')
obj.totalSalary=7000# print(obj.totalSalary()) #if we are not using @property we have to call the method than print it 
print(obj.salary)
print(obj.totalSalary)  #it print method in the form of property
print(obj.insentive)