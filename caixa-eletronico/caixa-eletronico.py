
print('='*30)
print(f'Caixa eletrônico')
print('='*30)
saque = float(input('Digite o valor para saque: '))
total = saque 
ced = 50.00
totalced = 0
cont = 0
while True:
    if total >=ced:
        total = total - ced
        totalced = totalced +1
        cont = cont +1
    else:
        if totalced > 0:
            print(f' {totalced} cedula de R${ced:.2f}')
        if ced == 50.00:
            ced = 20.00
        elif ced == 20.00:
            ced = 10.00
        elif ced == 10.00:
            ced = 5.00
        elif ced == 5.00:
            ced =1.00
        totalced = 0
        if total == 0:
            break
print(f'Quantidade de Cedula geral: {cont}')
print('='*30)