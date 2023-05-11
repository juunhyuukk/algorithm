nlist = [i for i in range(1,31)]

for i in range(28) :
    n = int(input())
    nlist.remove(n)

for i in nlist :
    print(i)