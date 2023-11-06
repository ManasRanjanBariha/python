str="SHIFT"

for i in range(len(str)+1):
    print(str)
    str=str[1:len(str)]+str[0]
