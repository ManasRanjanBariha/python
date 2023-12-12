def cal_electric_bil(unit):
    if(unit <=100):
        print("No charges")
    elif(unit <=200):
        print("bill=",(unit-100)*5)
    else:
        print("bill=",((unit-200)*10)+500)

cal_electric_bil(100)
cal_electric_bil(150)
cal_electric_bil(350)

