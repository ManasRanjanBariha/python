t=(1,2,3,4,53,5,4,3,6,3,1)
l=[]
for i in t:
    if t.count(i)> 1 and i not in l:
        print(i)
        l.append(i)
