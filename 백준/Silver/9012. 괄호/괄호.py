T = int(input())

for t in range (1, T+1) :
    stack = []
    PS = input()
    for n in PS :
        if n == '(' :
            stack.append(n)
        elif n == ')' :
            if len(stack) != 0 :
                stack.pop()
            else :
                print('NO')
                break
    else :
        if len(stack) == 0 :
            print('YES')
        else :
            print('NO')