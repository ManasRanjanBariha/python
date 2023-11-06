str=input("Enter a String ")
v='aeiou'
count =0
for i in str:
    if i in v:
        count+=1
print("The number of vowel in the string is ",count)
