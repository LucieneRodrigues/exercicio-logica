
'''Cria uma pirâmide dupla do Mário'''

print("\n")
n = int(input( 'Digite um numero entre 1 e 8: '))

while n < 1 or n > 8:
    print('Numero invalido, Digite um numero entre 1 e 8!')
    n = int(input('Digite um numero entre 1 e 8:'))
j = 0
i = n
while i <= n and j <= n:
    print(f'{" "*i:<}{"#"*j}{"  "}{"#"*j:>}{" "*i:>}')
    i = i -1
    j = j + 1
print("\n")
    