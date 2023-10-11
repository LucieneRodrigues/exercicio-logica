
'''Cifra de Cesar,Criptografia de Cesar desloca as letras de acordo com o numero da chave '''

texto = input('Digite a mensagem a ser encriptada ou decifrada: ').strip()
chave = str(input('Digite um valor inteiro para  chave de deslocamento: '))
while chave.isnumeric() == False:    
    print('Numero invalido, digite apenas numero, sem espaços')
    chave = str(input('Digite um valor inteiro para  chave de deslocamento: '))       
chave = int(chave)
modo = input('Escolha E para encriptar ou D para decriptar o texto: ').upper()
CARACTERES = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' # letras do alfabeto como referencia
CARACTERESMI = 'abcdefghijklmnopqrstuvwxyz'
CARACTERESESP = ',.!?:;'
CARACTERESV = ' '
num = 0
convertido = list()
for caractere in texto:
    if caractere in CARACTERES:
        num = CARACTERES.find(caractere) #posição dos caracterie       
        if modo == 'E':
            num = num + chave            
            if num >= len(CARACTERES):
                num = num - len(CARACTERES)               
            convertido.append(CARACTERES[num])          
        elif modo == 'D':
            num = num - chave          
            if num >= len(CARACTERES):
                num = num + len(CARACTERES)
            convertido.append(CARACTERES[num])
    elif caractere in CARACTERESMI:
        num = CARACTERESMI.find(caractere) #posição dos caracterie       
        if modo == 'E':
            num = num + chave            
            if num >= len(CARACTERESMI):
                num = num - len(CARACTERESMI)               
            convertido.append(CARACTERESMI[num]) 
        elif modo == 'D':
            num = num - chave          
            if num >= len(CARACTERESMI):
                num = num + len(CARACTERESMI)
            convertido.append(CARACTERESMI[num]) 
    elif caractere in CARACTERESESP:
        num = CARACTERESESP.find(caractere) #posição dos caracterie       
        if modo == 'E':
            num = num                         
            convertido.append(CARACTERESESP[num]) 
        elif modo == 'D':
            num = num            
            convertido.append(CARACTERESESP[num])
    elif caractere in CARACTERESV:
        num = CARACTERESV.find(caractere) #posição dos caracterie       
        if modo == 'E':
            num = num                          
            convertido.append(CARACTERESV) 
        elif modo == 'D':
            num = num            
            convertido.append(CARACTERESV[num])

a = ''.join(convertido) #tira os caracterie da lista e junta
if modo == 'E':
    print('O texto criptografado é ',a)
if modo == 'D':
    print('O texto decriptado é ',a)
