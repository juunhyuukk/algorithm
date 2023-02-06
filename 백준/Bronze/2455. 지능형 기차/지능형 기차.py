cnt = 0
lst = []

for i in range (4) :
    O, I = list(map(int,input().split()))
    cnt = cnt - O + I

    lst.append(cnt)
    
print(max(lst))