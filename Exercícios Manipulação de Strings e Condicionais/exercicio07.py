letra = input('DIGITE UMA LETRA:').upper()

if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print('ESSA LETRA É UMA VOGAL')
elif len(letra) > 0:
    print('LETRA INVÁLIDA')
else:
    print('ESSA LETRA É UMA CONSOANTE')