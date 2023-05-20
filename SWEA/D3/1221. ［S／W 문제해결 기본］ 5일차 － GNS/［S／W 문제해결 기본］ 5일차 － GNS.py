T = int(input())

for t in range(1,T+1) :
    N = input().split()

    num = list(map(str,input().split()))
    numlist = []
    ans = []

    for i in num :
        if i == 'ZRO' :
            i = int(0)
        elif i == 'ONE' :
            i = int(1)
        elif i == 'TWO' :
            i = int(2)
        elif i == 'THR' :
            i = int(3)
        elif i == 'FOR' :
            i = int(4)
        elif i == 'FIV' :
            i = int(5)
        elif i == 'SIX' :
            i = int(6)
        elif i == 'SVN' :
            i = int(7)
        elif i == 'EGT' :
            i = int(8)
        elif i == 'NIN' :
            i = int(9)
        numlist.append(i)

    numlist.sort()
    
    for i in numlist :
        if i == 0 :
            i = str('ZRO')
        elif i == 1 :
            i = str('ONE')
        elif i == 2 :
            i = str('TWO')
        elif i == 3 :
            i = str('THR')
        elif i == 4 :
            i = str('FOR')
        elif i == 5 :
            i = str('FIV')
        elif i == 6 :
            i = str('SIX')
        elif i == 7 :
            i = str('SVN')
        elif i == 8 :
            i = str('EGT')
        elif i == 9 :
            i = str('NIN')
        ans.append(i)
    
    print(f'#{t}')
    for i in ans :
        print(i,end = ' ')