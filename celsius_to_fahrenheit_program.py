celsius = int(input('Podaj ile stopni C:'))

def conv(c):
        c = celsius
        x = (c*9/5+32)
        return x


fahrenheit = conv(celsius)

print(celsius,"st. C, to", fahrenheit ,"st. F.")