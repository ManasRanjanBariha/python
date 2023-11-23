t=(10, 20, (20, 10), 30, (40, 50, 60), 60, 70)
t1=()
l=[]
for i in t:
    if type(i)== type(t1):
        for j in i:
            l.append(j)
    else:
        l.append(i)

res=[]
for i in l:
    if  i not in res:
        res.append(i)
        print(i,":",l.count(i),end=" ")
        print(",",end="")
