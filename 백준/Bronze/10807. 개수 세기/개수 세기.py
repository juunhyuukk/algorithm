N = int(input())
numbers = list(map(int,input().split()))
V = int(input())

cnt = 0

for i in numbers :
    if i == V :
        cnt += 1
print(cnt)