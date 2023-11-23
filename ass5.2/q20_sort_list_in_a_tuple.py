t=( [10, 50, 60], [80, 20, 30], [70, 100, 40], (90,) )
l=list(t)
print(type(l))
for i in range(0,len(l)):
    if(type(i)!=type(t)):
        l[i]=l[i].sort()
t=tuple(l)
print(t)
