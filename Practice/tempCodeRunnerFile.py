
# FizzBuzz problem 
# solution 1 with % operator
def FizzBuss(num):
    list3=[i*3 for i in range(num)]
    list5=[i*3 for i in range(num)]
    for i in range(1,num+1):
        if i%3==0:
            print("Fizz")
        elif i%5==0:
            print("Buzz")
        elif i in list3 and i in list5:
            print("FizzBuzz")
        else:
            print(i)
    return list3,list5
FizzBuss(15)