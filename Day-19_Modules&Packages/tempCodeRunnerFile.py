#4. check if it is a file or folder
path="D:\PythonProjects"
flist=os.listdir(path)
def check(p,l):
    for i in range(l):
        if os.path.isdir(os.path.join(p,i)):
            print("is is a folder")
        else:
            print("it is a file")
print(check(path,flist))