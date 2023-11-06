x=float(input("Enter a number"))
y=float(input("Enter a number"))

if x > y and x-y<=0.001:
    print("close")
elif x < y and y-x<=0.001:
    print("close")
else:
    print("Not close")
