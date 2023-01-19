nlist = []
sum = 0
oddlist = []

for i in range (0, 7):
    nlist.append(int(input()))
for n in nlist :
    if n % 2 == 1 :
        sum += n
        oddlist.append(n)

if len(oddlist) == 0 :
    print('-1')
else :
    print(sum)
    print(min(oddlist))