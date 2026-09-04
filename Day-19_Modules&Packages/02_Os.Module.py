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


