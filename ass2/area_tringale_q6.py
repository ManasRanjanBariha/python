a=float(input("Enter the first side of tringle"))
b=float(input("Enter the second side of tringle"))
c=float(input("Enter the third side of tringle"))

s=(a+b+c)/2

area= (s*(s-a)*(s-b)*(s-c)) ** 0.5

print("The area of the triangle is ",area)
