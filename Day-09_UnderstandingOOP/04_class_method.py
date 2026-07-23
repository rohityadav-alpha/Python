class employee:
    name="rohit"
    age=23
    salary=5500
    insentive=600
    company="google"

    @classmethod        #class method use to take class variables in methods
    def totalSalary(cls):
        cls.totalsalary=cls.salary+cls.insentive
        return print(cls.totalsalary)

obj=employee()
print(obj.salary)
obj.totalSalary()