t=( ('a', 53), ('b', 37), ('c', 23), ('d', 1), ('e', 18) )
tup=list(t)
print(t)
lst = len(tup)
for i in range(0, lst): 
    for j in range(0, lst-i-1):
        if (tup[j][1] > tup[j + 1][1]):
            temp = tup[j]
            tup[j] = tup[j + 1]
            tup[j + 1] = temp

t=tuple(tup)
print(t)
