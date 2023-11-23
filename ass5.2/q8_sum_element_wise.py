A = (2, 5, 8)
B = (6, 5, 1)
C = (1, 4, 7)
D = (3, 7, 2)
print("A",A)
print("B",B)
print("C",C)
print("D",D)
s=[]
for i in range(3):
    sum=A[i]+B[i]+C[i]+D[i]
    s.append(sum)
print("Sum of Elements = ",tuple(s))
