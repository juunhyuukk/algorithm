def recursive(a,b) :
    return(a**b)

for _ in range (1,11) :
    t = int(input())
    a, b = map(int,input().split())
    ans = recursive(a,b)

    print(f'#{t} {ans}')