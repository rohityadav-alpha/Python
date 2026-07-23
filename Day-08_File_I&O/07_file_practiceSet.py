'''#Q1. write a program to read the text from a file and find out
whether the file contains a specific word or not. with
open('poem.txt','r') as p: poem=p.read() if "dust" in poem: print("Yes!
the word 'Dust' is present in the poem file") else: print("No! the word
'Dust' is not present in the poem file")



"""
Q2.the game() function in a program let a user play a game and returens the
score as an integer you need to read a file 'hi-score.txt' which is
either blank or contains the previous hi-score you need to write a
program to update the hi-score you need to write a program to update the
hi-score whether game() break the hi-score"""
def game():
    return 2005
highscore=game()
with open("hiscore.txt") as h:
    record=h.read()
if record=="":
    with open('hiscore.txt','w') as h:
        h.write(str(highscore))
elif int(record)<highscore:
    with open('hiscore.txt','w') as h:
        h.write(str(highscore))



#Q3.write a program to generate multiplication tables of any number

num=int(input("enter the number:"))
with open(f'table\\table{num}.txt','w+') as t:
    for i in range(1,20+1):
        table=(f'{num} X {i} = {(num*i)}\n')
        t.write(str(table))
with open(f'table\\table{num}.txt','r+') as r:
    m=r.read()
    print(m)



#Q4.write a program to generate multiplication tables from 2 to 20 and write it to the different file, place these files in a folder for a 13-year old 
for i in range(2,21):
    with open(f'table\\table{i}.txt','w+') as t:
        for j in range(1,11):
            table=(f'{i} X {j} = {(i*j)}\n')
            t.write(str(table))



#Q5.a file contain a word "dust" multiple times  you
#need to write a program which replace this words with'#####' by updating the same file
list_word=["Dust","dust","Botanist","crooked"]

with open('poem.txt','r+') as p:
    r=p.read()
    
for word in list_word:
    r=r.replace(word,"#####")
    with open('poem.txt','w') as p:
        p.write(r)
    


#Q6.write a program to print a log file and find out whether it contain 'Attempting' at which line
line=True
i=1
with open("log.txt","r") as l:
    while line:
        line=l.readline()
        if 'Attempting' in line:
            print(line)
            print(i)
        i+=1


#Q7.write a program to make a copy of a text file "original.txt"
with open("sample.txt") as s:
    var=s.read()

with open("copy.txt","w") as s:
    s.write(var)
    


#Q8.write a program to find whether a files are identical or not
file1="sample.txt"
file2="copy.txt"
with open(file1,"r") as f1:
    file1=f1.read()
with open(file2,"r") as f2:
    file2=f2.read()

if file1==file2 :
    print("identical files")
else:
    print('not identical files')



#Q9.write a program to wipe out the contains of a file using python
with open("sample3.txt") as f:
    f.read()

with open("sample3.txt",'w') as f:
    f.write("")
'''


