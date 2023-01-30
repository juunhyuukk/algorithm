A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
D = list(map(int,input().split()))
E = list(map(int,input().split()))

sum = [sum(A), sum(B), sum(C), sum(D), sum(E)]
print(sum.index(max(sum))+1, max(sum))