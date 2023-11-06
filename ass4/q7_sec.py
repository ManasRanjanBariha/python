l1=[1,2,3,4,5,7,8,9]
large=max(l1)
small=min(l1)
lar2=small
sma2=large
for i in l1:
    if lar2 < i and i != large:
        lar2=i
    if sma2 > i and i !=small:
        sma2=i
print("second largest=",lar2)
print("second smallest=",sma2)
