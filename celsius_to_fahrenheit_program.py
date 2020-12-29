celsius = int(input())  

def conv(c):
        c = celsius
        x = (c*9/5+32)
        return x


fahrenheit = conv(celsius)

print(fahrenheit)