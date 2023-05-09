import sys
input = sys.stdin.readline

N, M = map(int,input().split())
num = list(map(int,input().split()))

sumlist = [0]
temp = 0

for i in num :
    temp = temp + i
    sumlist.append(temp)

for a in range (M) :
    i, j = map(int,input().split())
    print(sumlist[j] - sumlist[i-1])