item=int(input("Enter the item you are buying"))
if item <10:
    print("price=",item*12)
elif item < 99:
    print("price=",item*10)
elif item >= 100:
    print("price=",item*7)
