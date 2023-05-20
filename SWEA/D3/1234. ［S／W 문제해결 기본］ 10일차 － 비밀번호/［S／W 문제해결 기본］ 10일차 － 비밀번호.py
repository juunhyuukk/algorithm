T = 10

for t in range (1,T+1) :
    N, password = input().split()

    stack = []

    for i in password :
        if stack and stack[-1] == i :
            stack.pop()
        else :
            stack.append(i)
    
    ans = ''
    for i in stack :
        ans+=i

    print(f'#{t} {ans}')