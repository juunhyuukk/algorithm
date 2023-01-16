N1, N2, N3 = list(map(int,input().split()))
dice = [N1, N2, N3]

if N1 == N2 == N3 :
    print(10000+N2*1000)
elif N1 == N2 or N1 == N3 or N2 == N3 :
    if N1 == N2 or N1 == N3 :
        print(1000+N1*100)
    else :
        print(1000+N2*100)
elif N1 != N2 != N3 :
    print(max(dice)*100)