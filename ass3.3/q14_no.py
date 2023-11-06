str1=input("Enter a String")
str2=input("Enter another String")
print("value of str1=",str1,"\nvalue of str2=",str2)
res=str2[:len(str2)-1]+str1[len(str1)-1]+str1[:len(str1)-1]+str2[len(str2)-1]
print("res=",res)
