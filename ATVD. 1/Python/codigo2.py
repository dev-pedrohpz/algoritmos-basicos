

# valorA = float(input("Insira o valor A: "))
# valorB = float(input("Insira o valor B: "))

# verificacao = (valorA == 0 or valorB == 0)

# while verificacao == True:

#     valorA = float(input("Insira o valor A: "))
#     valorB = float(input("Insira o valor B: "))

#     if verificacao != True:
#         break

# print(valorA + valorB)    


# etrutura do while inicia aqui

valorA = float(input("Insira o valor A: "))
valorB = float(input("Insira o valor B: "))

while valorA == 0 or valorB == 0:
    print("Digite novamente essa tranqueira")
    valorA = float(input("Insira o valor A: "))
    valorB = float(input("Insira o valor B: "))

# e termina aqui, caso a condição seja desfeita, mas houve uma primeira interação já, lá no ínicio do código.

if (valorA > 10 and  valorB > 10):
    soma = valorA + valorB
    diferenca = valorA - valorB
    print(F"A soma dos valores é: {soma}") 
    print(F"A diferença dos valores é: {diferenca}")   

elif (valorA > valorB ):
    print(F"O valor {valorA} é maior que o valor {valorB}")

elif (valorB > valorA):
    print(F"O valor {valorB} é maior que o valor {valorA}") 

else:
    print(F"Os valores {valorA} e o {valorB} são iguais")    