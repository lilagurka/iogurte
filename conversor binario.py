#Conversor binario - Guilherme Rebellatto e Marina Silva
print (' - ' * 55)
esp = 0 



while True :
    tudo = ('') # Variavel começa vazia

    numero = int(input ('Digite um numero para ser convertido \n  '))
    neymar = numero

    

#---------------------------------------------------------------------------------------------------
    while (numero) > 0 :        # inicia o loop
        if numero % 2 == 0 :   # se numero for par....
            tudo = tudo + ('0')   # adicona zero
        else :
            tudo = tudo + ('1')  # senão adicona um

        numero = numero // 2 # divide o numero por dois

        if esp == 8:
            tudo = tudo + ' '
            esp = esp - 8
            
        esp = esp +1
#----------------------------------------------------------------------------------------------------


        
    if (numero) < 0 : print ('numero invalido')  # caso o numero seja negativo
    print ( neymar,  ' em binario é  :',   (tudo[::-1]) , '\n' )  # imprime o resultado final de tras pra frente

    mazzutti_fofo = str(input('deseja converter outro numero?  S/N')).upper()

    if mazzutti_fofo == 'S' : print ('')
    elif mazzutti_fofo == 'N':break
    else:  print ('?????????????????????????')
