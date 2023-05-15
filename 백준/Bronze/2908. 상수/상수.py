A, B = input().split()

A = A[2]+A[1]+A[0]
B = B[2]+B[1]+B[0]

a = int(A)
b = int(B)

if a < b :
    print(b)
else :
    print(a)