sum = 0

for i in range (1, 6) :
    i = int(input())
    
    if i < 40 :
        i = 40
        sum += i
    else :
        sum += i

print(sum // 5)
