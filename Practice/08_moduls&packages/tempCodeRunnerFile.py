# [EASY] Question 1.1: How do you check if a file or folder exists on disk and obtain its absolute path using `os.path`?
import os 
newfile=os.path.exists('Practice/08_moduls&packages/01-05_Que.py')
print(newfile)
path=os.path.abspath('README.md')
print(path)