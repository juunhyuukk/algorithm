str = input()

happy = str.count(':-)')
sad = str.count(':-(')

if happy < sad :
    print('sad')
elif happy == sad == 0 :
    print('none')
elif happy == sad :
    print('unsure')
else :
    print('happy')