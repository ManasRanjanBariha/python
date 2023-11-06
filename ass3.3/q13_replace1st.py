str=input("Enter the String")
str=str[0]+str[1:].replace(str[0],'$')
print("The replaced string is",str)
