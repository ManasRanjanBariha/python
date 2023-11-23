t=[ (4, 5, 5, 7), (1, 3, 7, 4), (19, 4, 5, 3), (1, 2) ]

for i in range(0,len(t)):
    for j in range(0,len(t)-i):
        if(max(t[i]) > max(t[j])):
            temp=t[i]
            t[i]=t[j]
            t[j]=temp
print(t)
