'''
f=open('sample.txt','r+') #it use for read first than write (file must be present)
file1=f.read()
update=f.write('updated adharcard')
f.close()
print(update,file1)


f=open('sample3.txt','w+') #it use for create&write first than read 
file1=f.write('updated adharcard with biomatrics')
data=f.read()
f.close()
print(data,file1)


f=open('sample3.txt','a+') #it use for create&write first than read 
file1=f.write('and address')
data=f.read()
print(data,file1)
f.close()
'''
