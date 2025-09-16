# Crie um programa que:

# Peça dois números inteiros positivos.
# Se os dois forem maiores que 10, calcule e mostre a soma e a diferença entre eles.
# Caso contrário, mostre apenas o maior entre eles.
# O programa deve repetir até que ambos os números digitados sejam maiores que 0.

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