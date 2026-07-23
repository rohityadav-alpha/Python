'''
# use with to skip writing close function .close
with open('sample.txt','a') as f:
    f.write(' file  with ')
    
with open('sample.txt','r') as f:
    data=f.read(10)
print(data)
'''
