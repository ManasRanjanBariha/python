str=input("Enter a String")
length=len(str)
count=0
print("the length of the String is ",length)
for i in range(length):
    if str[i] in 'aeiouAEIOU':
        count+=1
print("The number  vowels in the String is ",count)
