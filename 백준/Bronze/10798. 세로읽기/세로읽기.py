lst = []

for i in range (0, 5) : 
    lst.append(input())

for s in range (15) :
    for i in range (5) :
        if s < len(lst[i]):
            print(lst[i][s], end = '')