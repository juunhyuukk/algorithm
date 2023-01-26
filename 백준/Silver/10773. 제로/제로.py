K = int(input())
lst = []

for k in range (K) :
    N = int(input())

    if N == 0 :
        lst.pop()
    else :
        lst.append(N)
print(sum(lst))