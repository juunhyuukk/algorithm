T = 10

for t in range (1,T+1) :
    tc = int(input())
    find = input()
    word = input()
    cnt = 0

    for i in range (len(word)) :
        if word[i:i+len(find)] == find :
            cnt+=1
    print(f'#{t} {cnt}')