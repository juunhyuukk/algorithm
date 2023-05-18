T = int(input())

for t in range (1, T+1) :
    S = input()
    slist = ['a','e','i','o','u']
    
    for i in S :
        if i in slist :
            S = S.replace(i, '')
    print(f'#{t} {S}')