T = int(input())
score = list(map(float,input().split()))

M = max(score)
sum = 0

for i in score :
    sum += int(i) / M * 100

avg = sum/T

print(avg)