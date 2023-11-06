temp=float(input("Enter the temputer"))
unit=int(input("what unit it is ?\nentr 1 for  Fahrenheit enter 2 for Celsius "))
if unit==1:
    print("celcius:",9/5 * unit +32)
elif unit ==2:
    print("Fahrenheit:",5/9*(unit-32))
else:
    print("Invalid input")
