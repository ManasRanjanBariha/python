l=[ (1, 3, 5), (4, 5, 7), (1, 2, 6), (10, 9), (10,) ]
l=list((sum(l,())))
res=[]
for i in l:
    if l.count(i) == 1 and i not in res:
        res.append(i)

print(res)
