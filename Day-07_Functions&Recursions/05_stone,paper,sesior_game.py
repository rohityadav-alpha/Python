#import random module to choice random values
import random

you=input("Type your choise (stone,paper,scissor) : ")
you=you.lower()

print(f"you choosed {you}")
# #random choice method1 using random.choice function to choice string from list
# l1=["stone","paper","scissor"]
# com=random.choice(l1)

#random choice method2 using random.randint function to choice random number(integer)from the range (1,3)
randnum=random.randint(1,3)
com=0
if randnum==1:
   com="stone"
elif randnum==2:
   com="paper"
elif randnum==3:
   com="scissor"
    
print(f"computer choosed {com}")

#function to return false/true/none when i lose/win/tie respectively
def game(you,com):
    if you==com:    #---------when the compuert and your same than tie 
        return None
    
    elif com=="stone":   #----when the computer chooses stone 
        if you=="paper":
            return True
        elif you=="scissor":
            return False
        
    elif com=="paper":   #----when the computer chooses paper
        if you=="scissor":
            return True
        elif you=="stone":
            return False
        
    elif com=="scissor": #----when the computer chooses scissor
        if you=="stone":
            return True
        elif you=="paper":
            return False   

result1=game(you,com)   #----calling the function and storing the return value in result1 variable
if result1==None:
    print("tie")
elif result1==True:
    print("You Win")
elif result1==False:
    print("You Lose ")
    
