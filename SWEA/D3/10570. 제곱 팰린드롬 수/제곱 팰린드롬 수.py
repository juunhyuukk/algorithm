T = int(input())

for t in range (1, T+1) :
    A, B = map(int,input().split())
    cnt = 0

    for i in range (A, B+1) :
        rootnum = i**(1/2)

        if rootnum == int(rootnum) :
            i = str(i)
            rootnum = str(int(rootnum))

            if i == i[::-1] and rootnum == rootnum[::-1] :
                cnt += 1

    print(f'#{t} {cnt}')