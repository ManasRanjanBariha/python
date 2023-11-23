l=[1,2,3,5,('a','n','c'),6,67,9,4,3]
i=0;
t=()
n=len(l)
while(i<n):
    if type(t)==type(l[i]):
        break
    i+=1
print(i)
