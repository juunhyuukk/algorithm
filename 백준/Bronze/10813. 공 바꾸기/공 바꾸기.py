N, M = map(int,input().split())

slist = [0]*N
temp = 0

for i in range (N) :
    slist[i] = i+1

for i in range (M) :
    i, j = map(int,input().split())
    temp = slist[i-1]
    slist[i-1] = slist[j-1]
    slist[j-1] = temp

for i in slist :
    print(i, end=' ')