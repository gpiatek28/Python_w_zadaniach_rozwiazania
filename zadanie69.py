import random
tablica = []

x=0


while x<3:
    y =random.randint(1,80)
    tablica.append(y)
    tablica.sort()
    x+=1
print(tablica)
