N, M = map(int,input().split())

slist = [0]*N

for n in range (M) :
    i, j, k = list(map(int,input().split()))
    for a in range (i-1 ,j) :
        slist[a] = k

for i in slist :
    print(i, end=' ')