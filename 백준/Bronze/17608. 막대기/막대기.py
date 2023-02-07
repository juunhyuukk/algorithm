import sys
input = sys.stdin.readline

N = int(input())
lst = []
cnt = 1

for _ in range (N) :
    lst.append(int(input()))

max = lst[-1]

for i in range (len(lst)-1, -1, -1) :
    if lst[i] > max :
        cnt += 1
        max = lst[i]

print(cnt)