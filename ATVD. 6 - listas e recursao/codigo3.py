# Implemente a função recursiva da sequência de Fibonacci, 
# mas faça com que cada chamada da função imprima o valor de n que está sendo calculado.

def fibonacci(numero):
    if(numero == 1 or numero ==2):
        return 1
    else:
        return fibonacci(numero - 1) + fibonacci(numero-2)
        
posicao = int(input("Insira a posição do número que deseja saber o Fibonacci: "))
resultado = fibonacci(posicao)   
print(f"o valor de Fibonacci na posição {posicao} é: {resultado}")