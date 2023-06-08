import sys
input = sys.stdin.readline

n = int(input())

count_buy = list(map(int, input().split()))

lamen = [[0 for _ in range(3)] for _ in range(n)]

lamen[0][0] = count_buy[0]
count_buy[0] = 0

for i in range(n - 1):
    lamen[i][0] += count_buy[i]
    count_buy[i] = 0

    if count_buy[i+1] > lamen[i][0]:
        lamen[i+1][1] += lamen[i][0]
        count_buy[i+1] -= lamen[i][0]

    else:
        lamen[i+1][1] += count_buy[i+1]
        count_buy[i+1] -= lamen[i+1][1]

    if count_buy[i+1] > lamen[i][1]:
        lamen[i+1][2] += lamen[i][1]
        count_buy[i+1] -= lamen[i][1]

    else:
        lamen[i+1][2] += count_buy[i+1]
        count_buy[i+1] -= lamen[i+1][2]


lamen[n-1][0] = count_buy[n-1]

answer = 0

for i in range(n):
    for j in range(3):
        if j == 0:
            answer += lamen[i][j] * 3

        else:
            answer += lamen[i][j] * 2

print(answer)