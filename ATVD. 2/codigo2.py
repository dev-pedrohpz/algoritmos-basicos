# Crie um programa modularizado que receba a idade de uma pessoa e informe se ela pode ou não votar, considerando que:

# Menores de 16 anos não votam
# De 16 a 17 e maiores de 70, o voto é facultativo
# De 18 a 70, o voto é obrigatório
# Use pelo menos: uma função para verificar a faixa etária e um procedimento para imprimir a mensagem.

idadeUsuario = int(input("Insira a sua idade: "))
idade = idadeUsuario

situacao = ""
def verificacaoIdade(idade):
    if (idade < 16):
        situacao = "Não votam!"
    elif (idade = 16 or idade = 17):
        situacao = "Facultativo!"
    elif (idade > 70):
        situacao = "Facultativo!"
    elif (idade >= 18 and idade <= 70):
        situacao = "Obrigatório!"
    else:
        situacao = "Idade Inválida"

    return situação 

analise = verificacaoIdade

def idadeAvaliada(idade):
    print(verificacaoIdade)

print(idadeAvaliada(analise))