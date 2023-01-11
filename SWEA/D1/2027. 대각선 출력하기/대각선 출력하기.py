for a in range (1, 6) :
    for b in range (1, 6) :
            if a == b : 
                print('#', end='')
            else :
                print('+', end='')
                if b == 5 :
                    print('', end='\n')