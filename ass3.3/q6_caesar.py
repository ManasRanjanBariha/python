str=input("Enter a String ")
n=int(input("Enter the left shift value"))
print("The original String is ",str)
res=""
for i  in range(len(str)):
    ch=str[i]
    if ch.isupper():
        res+=chr((ord(ch)+n -65) % 26 +65)
    else:
        res+=chr((ord(ch)+n -97) % 26 +97)
print("The encypted String is ",res)
        
