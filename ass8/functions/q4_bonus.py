def bonus_cal(sal,exp):
    if(exp >10):
        return sal+(sal*0.1)
    elif(exp >=6):
        return sal+(sal*0.8)
    else:
        return sal+(sal*0.5)

print("bonus sal of emp 1 is",bonus_cal(25000,2))
print("bonus sal of emp 2 is",bonus_cal(55000,10))
print("bonus sal of emp 3 is",bonus_cal(55000,6))
print("bonus sal of emp 4 is",bonus_cal(25000,7))
