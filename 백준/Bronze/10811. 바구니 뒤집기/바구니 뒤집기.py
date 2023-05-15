N, M = map(int,input().split())
nlist = []

for i in range (1,N+1) :
    nlist.append(i)

for _ in range (M) :
    i, j = map(int,input().split())
    temp = nlist[i-1:j]
    temp.reverse()
    nlist[i-1:j] = temp

for i in range(N) :
    print(nlist[i], end = ' ')