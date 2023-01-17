Alist = []
Blist = []

for i in range (0, 3) :
    A, B = map(int,input().split())
    Alist.append(A)
    Blist.append(B)

for n in range(0, 3) :
    if Alist.count(Alist[n]) == 1 :
        x = Alist[n]
    if Blist.count(Blist[n]) == 1 :
        y = Blist[n]

print(x, y)