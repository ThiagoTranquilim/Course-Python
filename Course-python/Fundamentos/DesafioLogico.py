terca = True
quinta = True

if terca == True and quinta == True:
    print('TV 50p + sorvete')
else:
    if (terca == True and quinta == False) or (terca == False and quinta == True):
        print('TV 32p + sorvete')
    else:
        if terca == False and quinta == False:
            print('Saude')
