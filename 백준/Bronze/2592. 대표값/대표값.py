nlist = []

for i in range (0, 10) :
    num = int(input())
    nlist.append(num)
print(int(sum(nlist)/len(nlist)))

index = [0] * (max(nlist))

for n in nlist :
    index[n-1] += 1
print(index.index(max(index))+1)