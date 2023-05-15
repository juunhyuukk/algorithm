T = int(input())

for t in range (1,T+1) :
    date = input()
    year = date[0:4]
    mon = date[4:6]
    day = date[6:8]
    
    if int(mon) <= 0 :
        print(f'#{t} -1')
    if int(mon) > 12 :
        print(f'#{t} -1')
    if int(mon) == 1 or int(mon) == 3 or int(mon) == 5 or int(mon) == 7 or int(mon) == 8 or int(mon) == 10 :
        if int(day) > 31 :
            print(f'#{t} -1')
        else :
            print(f'#{t} {year}/{mon}/{day}')
    if int(mon) == 2 :
        if int(day) > 28 :
            print(f'#{t} -1')
        else :
            print(f'#{t} {year}/{mon}/{day}')
    if int(mon) == 4 or int(mon) == 6 or int(mon) == 9 or int(mon) == 11 :
        if int(day) > 30 :
            print(f'#{t} -1')
        else :
            print(f'#{t} {year}/{mon}/{day}')