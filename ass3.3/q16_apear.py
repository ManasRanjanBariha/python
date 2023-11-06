str=input("Enter a sentance")
p="poor"
n="not"
np=str.find(n)
if(np!=-1):
    str=str.replace(p,"good")
    str=str.replace(n,"")
print(str)
