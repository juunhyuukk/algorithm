T = int(input())

for t in range (1,T+1) :
    A, B = map(int,input().split())

    if A+B == 24 :
        print(f'#{t} 0')
    elif A+B > 24 :
        print(f'#{t} {A+B-24}')
    else :
        print(f'#{t} {A+B}')