frase = input('DIGITE UMA FRASE:')
c = input('DIGITE UM CARACTERE:')

if frase.find(c) != -1:
    print(f'ESSE CARACTERE APARECE {frase.count(c)} VEZES NA FRASE')
else:
    print('ESSE CARACTERE NÃO APARECE NA FRASE')