import os
import sys

#1. check if the file exists or not
if os.path.exists("README.md"):
    print("file exists")
else:
    print("file is not exists")


#2. print absolute path of the file
print(os.path.abspath("GreetModule.py"))
print(os.path.abspath(__file__)) # current file path


#3. join the directory and file name
File="read.txt"
basepath=os.path.abspath(__file__)
fullpath=os.path.join(basepath,File)
print(fullpath)


#4. check if it is a file or folder
path="D:\PythonProjects"
flist=os.listdir(path)
def check(p,l):
    for i in l:
        if os.path.isdir(os.path.join(p,i)):
            print(f"{i} :is is a folder")
        else:
            print(f"{i} :it is a file")
check(path,flist)