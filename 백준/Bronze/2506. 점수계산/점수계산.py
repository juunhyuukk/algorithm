N = int(input())
numbers = list(input().split())
score = 0
result = 0

for i in range (0, len(numbers)) :
    if numbers[i] == '1' :
        score += 1
        result += score
    else :
        score = 0
print(result) 