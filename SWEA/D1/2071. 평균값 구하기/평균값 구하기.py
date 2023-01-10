T = int(input())

for t in range(1, T+1) :
    numbers = list(map(float,input().split()))
    a = sum(numbers)
    b = len(numbers)
    avg = a/b
    print(f"#{t} {round(avg)}")