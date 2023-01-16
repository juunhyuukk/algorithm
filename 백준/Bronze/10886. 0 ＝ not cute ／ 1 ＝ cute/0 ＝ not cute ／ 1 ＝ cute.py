N = int(input())
cute = 0
ncute = 0

for n in range (1, N+1):
    V = int(input())
    if V == 1 :
        cute += 1
    else :
        ncute += 1

if cute > ncute :
    print("Junhee is cute!")
else :
    print("Junhee is not cute!")