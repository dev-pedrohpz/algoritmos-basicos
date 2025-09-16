# Escreva um programa que receba dois números do usuário, calcule a média entre eles e imprima a seguinte mensagem com base no valor:

# “Aprovado” se a média for maior ou igual a 6
# “Recuperação” se estiver entre 4 e 5.9
# “Reprovado” se for menor que 4
# O cálculo da média e a classificação devem ser feitos em funções/procedimentos separados.

valor1 = int(input("Insira o valor 1: "))
valor2 = int(input("Insira o valor 2: "))

def calculo_media(valorA, valorB):
    media = (valorA + valorB)/2
    return media
    
mediaValores = media
situacao = ""

def analise_media(mediaValores):
    if mediaValores >= 6:
        situacao = "Aprovado!"
    elif mediaValores > 4 and mediaValores < 5.9:
        situacao = "Recuperação!"
    else:
        situacao = "Reprovado!"
        
    return situacao
    
print(f"Pois sua média é de {mediaValores}, você está {situacao} ")