
filmy = []

while True:
    nazwa= input('Podaj nazwę ulubionego filmu, lub wpisz \"Koniec\", aby zakończyć')

    if nazwa == 'Koniec' or 'koniec':
        break
    filmy.append(nazwa)

print('Twoje ulubione filmy to:',filmy)

