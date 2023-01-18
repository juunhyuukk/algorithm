T = int(input())

for t in range (1, T+1) :
    R, S = input().split()
    for s in S :
        print(s*int(R), end='')
    print()