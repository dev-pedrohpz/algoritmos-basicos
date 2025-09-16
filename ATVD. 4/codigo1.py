# Crie uma função que receba dois números como parâmetros, retorne a soma deles e, no programa principal, 
# use o valor retornado para calcular e exibir o resultado da multiplicação dessa soma por 3.

v1 = int(input("Insira o valor 1: "))
v2 = int(input("Insira o valor 2: "))

def somaValores(valor1, valor2):
    return valor1 + valor2
   

resultado = somaValores(v1, v2)  #se passa os valores das variáveis que serviram de parametro onde irá ser armazenado o retorno, no caso, uma outra variável.

resultadoFinal = resultado * 3
print(f"O resultado da operação é {resultadoFinal}")