N = int(input())
nlist = []

for n in range (N) :
    nlist.append(int(input()))

nlist.sort()

for i in nlist :
    print(i)