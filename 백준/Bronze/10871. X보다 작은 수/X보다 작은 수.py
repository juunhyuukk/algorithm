N, X = map(int,input().split())
A = list(map(int,input().split()))

for i in range(0,len(A)) :
    if A[i] < X :
        print(A[i], end=' ')