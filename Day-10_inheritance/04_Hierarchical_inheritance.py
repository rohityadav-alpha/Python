class Info:
    country="indian"
    count_code="+91"

    def __init__(self,name,age,salary,occupation,gender,cast):
        self.name,self.age,self.salary,self.occupation,self.gender,self.cast=name,age,salary,occupation,gender,cast

class Personal(Info):

    def getPersonalInfo(self):
        print("child 1")
        print(f"Name: {self.name}  Age: {self.age}  Gender: {self.gender} ")

class Other(Info):
   def getEmpDetail(self):
    print("child 2")
    print(f"Salary: {self.salary}  Occupation: {self.occupation}  Cast: {self.cast}")

obj1=Personal("Rohit",23,50000,"Python dev","Male","Hindu")
obj2=Other("Rohit",23,50000,"Python dev","Male","Hindu")

obj1.getPersonalInfo()
print(f"Country code : {obj1.count_code}")

print("*************************")

obj2.getEmpDetail()
print(f"Country : {obj2.country}")

