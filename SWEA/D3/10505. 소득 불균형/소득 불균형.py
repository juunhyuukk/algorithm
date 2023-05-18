T = int(input())

for t in range (1, T+1) :
    N = int(input())
    income = list(map(int,input().split()))

    cnt = 0
    avg = sum(income)/len(income)

    for i in income :
        if i <= avg :
            cnt += 1
    print(f'#{t} {cnt}')