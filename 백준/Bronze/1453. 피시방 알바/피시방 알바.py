N = int(input())
num = list(map(int,input().split()))
cnt = 0
lst = []
for n in range (N) :
    if num[n] in lst :
        cnt += 1
    else :
        lst.append(num[n])
print(cnt)