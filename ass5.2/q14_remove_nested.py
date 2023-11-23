t=(10, 20, (30,), 40, (50, 60), 70)
l=[]
tt=()
for i in t:
    if type(i) != type(tt):
        l.append(i)

t=tuple(l)
print(t)
    
