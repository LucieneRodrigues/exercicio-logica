
'''Algoritmo de Luhn/ validação de cartão de crédito'''

print()
numcartao = str(input("Digite o número do cartão: ")).strip()
while numcartao.isnumeric() == False:    
    print('Numero invalido, digite apenas numero, sem espaços')
    numcartao = str(input("Digite o número do cartão: ")).strip()
  
if len(numcartao) < 10 or len(numcartao) > 16:
    print('Numero inválido')
   
else:
    
    numinteiro = int(numcartao)
    resto_divisao= 1
    resto_numero = numinteiro//resto_divisao %10
    lista = list()
    cont = 0
    while cont < len(numcartao):
        lista.insert(0,resto_numero)
        resto_divisao = resto_divisao*10
        resto_numero = numinteiro//resto_divisao %10
        cont = cont + 1

    lista1 = list()
    lista1_1 = list ()
    lista2 = list()
    somalista1_1 = 0
    for i, v in enumerate(lista):
        if i % 2 ==0:
            valor = v*2
            if valor > 9:
                lista1_1.append(valor)
                somalista1_1 = 0
                for i, v  in enumerate(lista1_1):
                    somalista1_1 = somalista1_1 + lista1_1[i]//1%10
                    somalista1_1= somalista1_1 + lista1_1[i]//10%10

            else:
                lista1.append(valor)

        elif i % 2 != 0:
            lista2.append(v)

    somalista1 = 0
    for i, v in enumerate(lista1):
        somalista1 = somalista1+ v

    somalista2 = 0
    for i, v in enumerate(lista2):
        somalista2 = somalista2 + v
    soma = somalista1 + somalista2 + somalista1_1
    final = soma//1%10
    print(f'O número digitado foi: {lista}')  

    if final == 0:
        print('Cartão Cadastrado com sucesso!')   
        if lista[0] == 4:
            print('Visa')
        elif lista[0] == 5 and lista[1] == 1 or lista[0] == 5 and lista[1] == 2 or lista[0] == 5 and lista[1] == 3 or lista[0] == 5 and lista[1] == 4 or lista[0] == 5 and lista[1] == 5:
           print('MasterCard')
    else:
        print('Cartão inválido!')
print()
     
     