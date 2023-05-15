N = int(input())
ans = []

for i in range (1,N+1) :
    if N%i == 0 :
        ans.append(i)

for i in ans :
    print(i, end=' ')