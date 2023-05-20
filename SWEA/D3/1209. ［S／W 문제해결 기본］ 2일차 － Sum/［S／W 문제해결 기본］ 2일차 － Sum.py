T = 10

for _ in range (1, T+1) :
    t = int(input())
    sumlist = []
    arr = []
    for i in range (100) :
        arr.append(list(map(int,input().split())))

    #가로, 세로줄의 합
    for i in range (100) :
        rowsum = 0
        colsum = 0
        for j in range(100) :
            rowsum += arr[i][j]
            colsum += arr[j][i]
            sumlist.append(rowsum)
            sumlist.append(colsum)
    
    #대각선의 합
    for i in range (100) :
        crosssum = 0
        revcrosssum = 0
        for j in range (100) :
            if i == j :
                crosssum += arr[i][j]
                sumlist.append(crosssum)
            revcrosssum += arr[i][99-j]
            sumlist.append(revcrosssum)
    
    print(f'#{t} {max(sumlist)}')