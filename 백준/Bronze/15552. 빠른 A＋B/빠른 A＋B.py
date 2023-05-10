import sys
input = sys.stdin.readline

T = int(input())
for t in range (T) :
    a, b = list(map(int,input().split()))
    print(a+b)