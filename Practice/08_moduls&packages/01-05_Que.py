# Module 1: File System & Path Operations (`os`, `sys`, `os.path`)

# [EASY] Question 1.1: How do you check if a file or folder exists on disk and obtain its absolute path using `os.path`?
import os 
newfile=os.path.exists('README.md')
print(newfile)
path=os.path.abspath('README.md')
print(path)



# [EASY] Question 1.2: How do you safely join directory paths and filenames without hardcoding backslashes or forward slashes using `os.path.join`?
base_folder='C:\\Users\\User\\Documents'
filename="example.txt"
complete_path=os.path.join(base_folder,filename)
print(complete_path)



# [MEDIUM] Question 1.3: How do you scan a directory with `os.listdir()`, distinguish between files and folders using `os.path.isdir()`, and get file sizes with `os.path.getsize()`?
Listofdir=os.listdir('D:\\PythonProjects')
path='D:\\PythonProjects'
print(Listofdir)
for item in Listofdir:
    full_path=os.path.join(path,item)
    if os.path.isdir(full_path):
        print(f'{item} is a folder, size: {os.path.getsize(full_path)} bytes')
    else:
        print(f'{item} is a file, size: {os.path.getsize(full_path)} bytes')




# [MEDIUM] Question 1.4: How do you safely rename a file with `os.rename()` and delete files vs empty folders using `os.remove()` and `os.rmdir()`?
fullpath="D:\\LEARN_PYTHON\\Practice\\08_moduls&packages"
# rename file
if os.path.exists(os.path.join(fullpath,"xyz.txt")):
    os.rename(os.path.join(fullpath,"xyz.txt"),os.path.join(fullpath,"rohit.txt"))
else:
    pass
# delete file 
if os.path.exists(os.path.join(path,"experiment.py")):
    os.remove(os.path.join(path,"experiment.py"))
else:
    pass 
# delete directpry
if os.path.exists(path):
    os.rmdir(path)
else:
    pass