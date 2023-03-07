import math

while True:
    a = float(input('Podaj wartość a: '))
    b = float(input('Podaj wartość b: '))
    c = float(input('Podaj wartość c: '))

    delta = b ** 2 - 4 * a * c

    if delta > 0:
        x1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        x2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print(f'Równanie ma dwa pierwiastki: {x1}, {x2}')
    elif delta == 0:
        x = -1 * b / (2 * a)
        print(f'Równanie ma jeden pierwiastek: {x}')
    else:
        print('Równanie nie ma pierwiastków rzeczywistych.')

    koniec = input('Czy chcesz zakończyć program? [T/N] ')

    if koniec.upper() == 'T':
        break

print('Koniec programu.')