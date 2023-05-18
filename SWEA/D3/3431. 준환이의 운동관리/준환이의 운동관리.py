T = int(input())

for t in range (1, T+1) :
    L, U, X = map(int,input().split())

    if X > U :
        print(f'#{t} -1')
    elif X < L :
        print(f'#{t} {L-X}')
    else :
        print(f'#{t} 0')