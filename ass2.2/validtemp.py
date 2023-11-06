temp=float(input("Enter the tempature in Celsius"))
if temp < -273.15:
    print("the temperature is invalid because it is below absolute zero")
elif temp == -273.15:
    print("the temperature is absolute 0")
elif temp > -273.15 and temp <=0:
    print("that the temperature is below freezing. • If it is 0,")
elif temp > 0 and temp < 100 :
    print("the temperature is in the normal range")
elif temp == 100 :
    print("that the temperature is at the boiling point. ")
elif temp > 100:
    print("the temperature is above the boiling point")
