str=input("Enter a String")
if(len(str)<2):
    print("Empty String")
else:
    print(str[0:2]+str[len(str)-2:len(str)])
    
