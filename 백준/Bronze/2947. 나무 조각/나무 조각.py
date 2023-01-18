S = list(map(int,input().split()))

while(True) :
    if S[0] > S[1] :
        S[0], S[1] = S[1], S[0]
        for s in S :
            print(s, end = ' ')
        print()
    if S[1] > S[2] :
        S[1], S[2] = S[2], S[1]
        for s in S :
            print(s, end = ' ')
        print()
    if S[2] > S[3] :
        S[2], S[3] = S[3], S[2]
        for s in S :
            print(s, end = ' ')
        print()
    if S[3] > S[4] :
        S[3], S[4] = S[4], S[3]
        for s in S :
            print(s, end = ' ')
        print()
    if S == [1, 2, 3, 4, 5] :
        break
    else :
        continue