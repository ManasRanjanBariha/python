str=input("Enter any sentence")
l=str.split()
max=0
word=""
for i in l:
    if max  <len(i) :
        max=len(i)
        word=i
print("Longest word=",word,"\nLongest length=",max)
