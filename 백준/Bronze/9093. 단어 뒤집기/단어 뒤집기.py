T = int(input())

for t in range(1, T+1) :
    S = list(input().split())
    for s in S :
        print(s[::-1], end = ' ')