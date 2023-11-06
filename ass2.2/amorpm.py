hour=int(input("Enter the hour between 1 to 12"))
ap=input("Enter am or pm")
future=int(input("Enter how many hours into the future they want to go "))

if "am" in ap:
    if(future > 12-hour):
        future-= 12 - hour
        print("Time =",future,"pm")
    else:
        print("Time=",future+hour,"am")
else:
    if( future > 12 -hour):
        future -=12-hour
        print("Time =",future,"am")
    else:
        print("Time=",future+hour,"pm")
    
