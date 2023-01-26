T = int(input())

for t in range (1, T+1) :
    Q = 25
    D = 10
    N = 5
    P = 1
    A = int(input())
    print(A//Q, A%Q//D, A%Q%D//N, A%Q%D%N)