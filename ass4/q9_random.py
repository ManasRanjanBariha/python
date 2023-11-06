import random
mi=int(input("Enter the minimum range"))
m=int(input("Enter the maximum range"))
l1=[]
for i in range(10):
    l1.append(random.randint(mi,m))
print(l1)
