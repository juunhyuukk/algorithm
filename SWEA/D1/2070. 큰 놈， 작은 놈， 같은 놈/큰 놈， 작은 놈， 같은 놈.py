T = int(input())

for t in range (1,T+1) :
    A, B = map(int,input().split())
    if A < B :
        print(f'#{t} <')
    elif A == B :
        print(f'#{t} =')
    else :
        print(f'#{t} >')