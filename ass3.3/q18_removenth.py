str=input("enter a String")
n=int(input("Enter index of the charecter you want to remove"))
if n<len(str) and len(str)!=0:
    print(str[:n])
    print(str[:n]+str[n+1:])
else:
    print("INVALID INPUT")

