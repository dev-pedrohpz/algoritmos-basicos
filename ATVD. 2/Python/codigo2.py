valoresSomados = []
valoresImpares = []
quantidadeValoresSomados = 0
for i in range(0, 5):
    valor = int(input("Insira um valor: "))
    valorPar = valor %2 == 0
    if(valorPar):
        valoresSomados.append(valor)
        quantidadeValoresSomados+=1 ## usado para incrementar uma variável global, nesse caso, contar a quantidade de números aptos para se somar e que são pares.

    elif(valorPar != True):
        print("o número é ímpar!")
        valoresImpares.append(valor)
    
somaTotal = sum(valoresSomados)
print(f"A soma dos valores {valoresSomados} é {somaTotal}, são {quantidadeValoresSomados} valores para se somar")
