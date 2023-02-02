Wlist = []
Klist = []
wsum = 0
ksum = 0

for i in range (1, 11) :
    Wlist.append(int(input()))

for i in range (1, 11) :
    Klist.append(int(input()))

Wlist.sort(reverse=True)
Klist.sort(reverse=True)

for i in range (0,3) :
    wsum += Wlist[i]
    ksum += Klist[i]

print(wsum, ksum)