#Operators in pyton can be overloded using dunder methods 
#Arithmetic Operators
# class number:
#     def __init__(self,num):
#         self.num=num

#     def __add__(self,num1): #sum operator overloded there using __add__ dunder method
#         return self.num + num1.num

#     def __mul__(self,num1):    #sum operator overloded there using __mul__ dunder method
#         return self.num * num1.num

#     def __sub__(self,num1):   #sum operator overloded there using __sub__ dunder method
#         return self.num - num1.num

#     def __truediv__(self,num1):   #sum operator overloded there using __division__ dunder method
#         return self.num / num1.num

#     def __floordiv__(self,num1):   #sum operator overloded there using __floordivision__ dunder method
#         return self.num // num1.num

#     def __pow__(self,num1):
#         return self.num**2 

# n1=number(50)
# n2=number(10)
# print('number object sum')
# Sum=n1+n2
# print(Sum)
# print('number object substraction')
# sub=n1-n2
# print(sub)
# print('number object multiplication')
# mul=n1*n2
# print(mul)
# print('number object division')
# div=n1/n2
# print(div)
# print('number object floor devision')
# fld=n1//n2
# print(fld)
# print('number object power number^2')
# Pow=n1**2 
# print(Pow)

#Comparision Operators
class Comp:

    def __inti__(self,num):
        self.num=num

    def __lt__(self,num1):
        return self.num < num1.num

    def __le__(self,num1):
        return self.num <= num1.num

n1=Comp(5)
n2=Comp(6)

# LessThen=n1<n2
# print(LessThen)
print(n1<n2)

# LessThenEqualTo=n1<=n2
# print(LessThenEqualTo)
print(n1<=n2)