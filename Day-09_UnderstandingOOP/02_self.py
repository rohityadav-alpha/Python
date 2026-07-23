#what is the purpos of using self argument in class method
class Employee:
    def company(self): #here self ensure that rohit is given
        print("company='google'") 
    
rohit=Employee()
rohit.company() #meaning of the line is Employee.company(rohit)