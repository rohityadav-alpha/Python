#(num:int) -- it is a type hint is indicates that the value shoud be integer
# -> it indicates the return type like str,int,or boolean
#integer addition 
def addition(a:int,b:int)-> int:
    return a+b
print(f"addition of number is {addition(4,5)}")

#string
def Greet(name:str)->str:
    return f"hello {name}" 
print(Greet("rohit"))

#float
def CubeRoot(num:float)->float:
    return num**1/3
print(f"cuberoot is {CubeRoot(8)}")

#boolean
def IsStudentIsAudult(num:int)->bool:
    return num>=18
print(f"the person is 18+ {IsStudentIsAudult(8)}")
print(f"the person is 18+ {IsStudentIsAudult(19)}")