

''' índice Coleman-Liau / O índice Coleman-Liau de um texto é projetado para mostrar qual nível escolar nos (EUA)
é necessário para entender o texto.
Fórmula: L = Letras ÷ Palavras × 100
         S = Frases ÷ Palavras × 100 '''

texto = str(input('Digite o texto:')).upper().strip()
lista = texto.split()
len(''.join(lista))
quant_palavras = 0
lista_letra0 = list()
lista_letra1 = list()
lista_letra2 = list()
excluir = texto.count('!') + texto.count('.') + texto.count('?') + texto.count(':') + texto.count('-') + texto.count('(') + texto.count(')') + texto.count('"') + texto.count(';') + texto.count(',') + texto.count("'")
for i, l in enumerate(lista):
    quant_palavras = len(lista) # quant palavas     
    if l.count('!') > 0:
        lista_letra0.append(l[-1].count('!'))
    elif l.count('?') > 0:
        lista_letra1.append(l[-1].count('?'))
    elif l.count('.') > 0:
        lista_letra2.append(l[-1].count('.'))
frase0 = 0
for i, v in enumerate(lista_letra0):
    frase0 = frase0 + v
frase1 = 0
for i, v in enumerate(lista_letra1):
    frase1 = frase1 + v
frase2 = 0
for i, v in enumerate(lista_letra2):
    frase2 = frase2 + v
frase = frase0 + frase1 + frase2 # setença
 
letra = len(''.join(lista)) - excluir

numero_letras_medio_cem_palavras =letra /quant_palavras * 100
numero_medio_frase_cem_palavras = frase / quant_palavras *100 

indice = 0.0588 * numero_letras_medio_cem_palavras - 0.296 * numero_medio_frase_cem_palavras - 15.8
grade= round(indice)

if grade < 1:
    print(' Grade menor que 1')
elif grade > 1 and grade < 2:
     print('Grade 1')

elif grade >= 2 and grade < 2.5:
    print('Grade 2')
    
elif grade > 2.5 and grade < 3.5:
    print('Grade 3')

elif grade > 3.5 and grade < 5.5:
    print('Grade 5')
    
elif grade > 5.5 and grade < 7.5:
    print('Grade 7')
    
elif grade > 7.5 and grade < 8.5:
    print('Grade 8')

elif grade > 8.5 and grade < 9.5:
    print('Grade 9')
    
elif grade > 9.5 and grade < 16:
    print('Grade 10')
    
elif grade >= 16:
    print('Grade 16+')




  