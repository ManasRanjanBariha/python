p=float(input("Enter the principle amount"))
t=float(input("Enter the time in years"))
r=float(input("Enter the rate of intrest"))
si=(p*t*r)/100
ci=p*(1+r/100)**t -p
print("SI=",si,"\nCI=",ci)
