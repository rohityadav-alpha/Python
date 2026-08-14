li1=[4,9,'h',8,'r',3,'o',3,4,'r']
li2=['o',9,3,7,'i',1,'i',9,'r','t','t']
def removeDuplicate(l1,l2):
    nlist=[]
    for i in l1:
        if i not in nlist:
            nlist.append(i)
    for j in l2:
        if j not in nlist:
            nlist.append(j)
    return print(nlist)
removeDuplicate(li1,li2)