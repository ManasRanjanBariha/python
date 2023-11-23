l = [ (18, 23), (2, 9), (7, 6), (9, 2), (10, 2), (23, 18) ]
l1=[]
for i in l:
    t=i[::-1]
    if t in l and  i not in l1:
        l1.append(t)

print(l1)
