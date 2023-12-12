def speed_check(speed):
    if(speed < 70):
        print("OK")
        return
    speed-=70
    point=speed/5;
    if(point < 12):
        print("points: ",point)
    else:
        print("License suspended")

speed_check(60)
speed_check(100)
speed_check(600)
