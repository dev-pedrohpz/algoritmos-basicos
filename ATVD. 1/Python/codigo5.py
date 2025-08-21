numeros = []
numerosNaoRequisitos = []
requisitosOk = []

for i in range(0, 6):
    numero = int(input("Insira o valor"))
    numeros.append(numero)

    par = numero %2 == 0
    positivo = numero > 0 
    negativo = numero < 0
    betweenHundred = numero >= 0 and numero < 100

    if(par == True and betweenHundred == True):
        print("Cumpriu todos os requisitos")
        requisitosOk.append(numero)
    else:
        print("Não cumpriu todos os requisitos.")   
        numerosNaoRequisitos.append(numero) 

print(F"Os com requisitos completos: {requisitosOk}")
print(F"Os com requisitos não completos: {numerosNaoRequisitos}")


    # if (numero %2 == 0):
    #     print("O número é par")
    #     numerosP.append(numero)
    # else:
    #     print("O número é ímpar") 
    #     numerosN.append(numero)
        





        
           

    