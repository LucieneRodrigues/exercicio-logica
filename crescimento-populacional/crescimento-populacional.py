'''crescimento populacional/ Quantos anos leva para atingir a quantidade final'''

n = int(input('Digite o tamanho da população inicial, maior que 9: '))
if n < 9:
    print('Dados inválido!')
    n = int(input('Digite o tamanho da população inicial, maior que 9: '))
novano = n//3
morano = n//4
ano = n+novano-morano
n1 = int(input('Digite o numero da população final, maior que 9:'))
if n1 < 9:
    print('Dados inválido!')
    n1 = int(input('Digite o tamanho da população inicial, maior que 9: '))
else:
    cont = 1 
    while ano < n1:
        ano = ano + ano//3  - ano//4
        cont = cont + 1
print(f'Será necessário {cont} ano(s) para atingir a população final desejada!')


