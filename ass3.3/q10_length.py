STR = input("Enter a String")
if(len(STR)<2):
    print("Empty String")
else:
    st=STR[0:2]+STR[-2:]
    print(st)
