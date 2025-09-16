# Crie uma função recursiva que calcule a soma dos dígitos de um número inteiro.

# Exemplo: soma_digitos(1234) → 1+2+3+4 = 10

def somaAlgarismos(numero):
    if numero < 10:
        return numero
    else:
        return numero % 10 + somaAlgarismos(numero // 10)

valor = int(input("Digite o número que deseja somar os algarismos: "))
resultado = somaAlgarismos(valor)
print(f"A soma total dos dígitos é: {resultado}")