T = int(input())

for t in range (1, T+1) :
    N = int(input())
    num = list(map(int,input().split()))
    print(sum(num))