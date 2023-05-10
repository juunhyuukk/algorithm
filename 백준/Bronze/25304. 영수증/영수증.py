X = int(input())
N = int(input())

sum = 0

for i in range (N) :
    a, b = list(map(int,input().split()))
    sum += a*b

if sum == X :
    print('Yes')
else :
    print('No')