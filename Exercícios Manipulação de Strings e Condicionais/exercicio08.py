palavra = input('DIGITE UMA PALAVRA:').strip()

if len(palavra) <= 4:
    print('ESSA PALAVRA É CURTA')
elif len(palavra) <= 8:
    print('ESSA PALAVRA É MÉDIA')
else:
    print('ESSA PALAVRA É LONGA')