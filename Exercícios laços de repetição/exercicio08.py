positivos = 0
negativos = 0
zeros = 0
for i in range(1,11):
    numero = int(input('DIGITE UM NÚMERO: '))
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos +=1
    else:
        zeros +=1
print(f'NÚMEROS POSITIVOS: {positivos}')
print(f'NÚMEROS NEGATIVOS: {negativos}')
print(f'NÚMEROS IGUAIS À ZERO: {zeros}')
