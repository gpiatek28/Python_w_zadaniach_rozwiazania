coffee = ['Cafe Latte', 'Caffe Americano', 'Espresso', 'Cappucino', 'Macchiato']

x=0
for i in coffee:
        print(x, coffee[x])
        x+=1
choice = int(input('Wybierz dostępną kawę:'))

try:
        if coffee[choice] in coffee:
                print(coffee[choice])

except IndexError:
        print('Invalid number')
finally:
        print('Have a good day')