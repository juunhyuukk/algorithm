N = int(input())
nlist = []

for i in range (N+1) :
    nlist.append(i)
    nlist.sort(reverse=True)

for i in nlist :
    print(i,end=' ')