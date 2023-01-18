S = input()
cnt = 0

for s in S :
    cnt += 1
    for c in range(11, cnt+1, 10):
        if cnt == c :
            print()
    print(s, end = '')