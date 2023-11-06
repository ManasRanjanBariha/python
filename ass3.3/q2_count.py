str=input("Enter a String")
length=len(str)
upr=0
lwr=0
white=0
digit=0
for i in range(length):
    if str[i].isupper():
        upr+=1
    elif str[i].islower():
        lwr+=1
    elif str[i].isdigit():
        digit+=1
    elif str[i] == ' ':
        white+=1
print("The number of uppercase letters in the string=",upr)
print("The number of lowercase letters in the string=",lwr)
print("The number of digits in the string=",digit)
print("The number of whitespace characters in the string=",white)
