# Crie uma calculadora que:

# Tenha funções para soma, subtração, multiplicação e divisão.
# O usuário escolhe a operação em um menu.
# Deve ser possível realizar vários cálculos, sendo informada uma opção para encerrar o programa.

def main():

    valorA = int(input("Insira o primeiro valor: "))

    valorB = int(input("Insira o segundo valor: "))

    situacao = ""

    print("1 - Adição ")
    print("2 - Subtração ")
    print("3 - Multiplicação ")
    print("4 - Divisão ")
    escolha = int(input("Insira o número da operação que você quer realizar: "))


    # Variáveis boleanas para armazenar as escolhas de operação

    adicao = 1

    sub = 2

    mult = 3

    div = 4

    # Funções da calculadora

    def soma(valor1, valor2):

        return valor1 + valor2

    def subtracao(valor1, valor2):

        return valor1 - valor2

    def multiplicacao(valor1, valor2):

        return valor1 * valor2

    def divisao(valor1, valor2):

        return valor1 / valor2

   

    # Estrutura de escolha para o usuário escolher a operação

    if(escolha == adicao):

        situacao = soma(valorA,valorB)

    elif(escolha == sub):

        situacao = subtracao(valorA,valorB)

    elif(escolha == mult):

        situacao = multiplicacao(valorA,valorB)

    elif(escolha == div):

        situacao = divisao(valorA,valorB)

    else:

        print("Insira um valor novamente: ")

   

    print(f"O resultado da operação é {situacao}")
    print("voltando pra tela de ínicio...")

while True:

    print("1 - Ir para a Calculadora")

    print("2 - Sair")

    opcao = int(input("Escolha uma opção: "))

    opcaoSair = 2

    opcaoCalc = 1

    if(opcao == opcaoSair):

        print("Você saiu do programa.")

        break

    elif(opcao == opcaoCalc):

        print("Indo pra calc...")

        main()

    else:

        print("Valor inválido, digite novamente.")        