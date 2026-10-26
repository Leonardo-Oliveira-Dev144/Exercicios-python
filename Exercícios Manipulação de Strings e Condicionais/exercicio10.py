palavra = input('DIGITE UMA PALAVRA:')

if palavra[::1] == palavra[::-1]:
    print('ESSA PALAVRA É UM PALÍNDROMO')
else:
    print('ESSA PALAVRA NÃO É UM PALÍNDROMO')