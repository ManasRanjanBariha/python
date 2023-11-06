str=input("Enter a String")
l1=[]
for i in str.split():
    l1.append(i[0].upper()+i[1:len(i)-1]+i[-1].upper())
print(l1)
