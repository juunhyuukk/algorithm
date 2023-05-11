remlist = []
cnt = 0

for i in range(10) :
    n = int(input())
    n %= 42
    remlist.append(n)

remlist = set(remlist)
print(len(remlist))