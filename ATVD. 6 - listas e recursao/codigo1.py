# Implemente uma função recursiva que receba dois números inteiros: um início e um fim.
# A função deve imprimir todos os números de início até fim, crescendo ou decrescendo conforme os valores.

# Exemplo: contar(3, 7) → imprime 3 4 5 6 7

# Exemplo: contar(7, 3) → imprime 7 6 5 4 3

intervalo = []

def contadorNumero(n1, n2):
 
    print(n1)
    if(n1 == n2):
        intervalo.append(n2)
        return intervalo
    elif(n1 < n2):
        intervalo.append(n1)
        return contadorNumero(n1 +1, n2)
    elif(n1 > n2):
        intervalo.append(n1)
        return contadorNumero(n1 -1, n2)

valor1 = int(input("Insira o valor 1: "))
valor2 = int(input("Insira o valor 2: "))

intervalos = contadorNumero(valor1, valor2)
print(f"O intervalo entre o valor {valor1} e o valor {valor2} são: {intervalo}")    