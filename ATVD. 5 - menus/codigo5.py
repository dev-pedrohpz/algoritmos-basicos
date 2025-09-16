# Crie um arquivo de funções utilitárias que contenha:

# eh_par(n ) → retorna se um número é par.
# fatorial(n ) → calcula o fatorial.
# maior_de_tres(a, b, c) → retorna o maior número.
# Depois, crie um programa que use essas funções para resolver diferentes cálculos escolhidos pelo usuário.

def main():
    
    def verificadorNumeroPar(valor):
        situacao = ""
        if(valor % 2 == 0):
            situacao = "É par!"
            return situacao 
        else:
            situacao = "Não é par!"
            return situacao 
    
    def fatorial(valor):
        print(valor)
        if(valor == 1):
            print("Fatorial acabou!")
            return valor
        else:
            return valor * (fatorial(valor - 1))
    
    def maiorDeTres(valorA, valorB, valorC):
        valores = [valorA, valorB, valorC]
        numeroMaior = max(valores)
        return numeroMaior
        
    def escolhaUsuario():
        print("Operações disponíveis: ")
        print("1 - verificar número par")
        print("2 - fazer fatorial ")
        print("3 - verificar número maior entre 3 valores ")
        escolhaU = int(input("Insira a sua escolha: "))
        
        if(escolhaU == 1):
            print("Indo para a verificação de número Par")
            valorA = int(input("Insira o valor: "))
            resultado = verificadorNumeroPar(valorA)
            print(resultado)
        
        elif(escolhaU == 2):
            print("Indo para o Fatorial")
            valorA = int(input("Insira o valor: "))
            resultado = fatorial(valorA)
            print(resultado)
            
        elif(escolhaU == 3):
            print("Verificar número maior entre 3 valores")
            valorA = int(input("Insira o primeiro valor: "))
            valorB = int(input("Insira o segundo valor: "))
            valorC = int(input("Insira o terceiro valor: "))
            resultado = maiorDeTres(valorA, valorB, valorC)
            print(resultado)
            
        else:
            print("Valor incorreto. Insira novamente...")
            return escolhaUsuario()
        
    escolhaUsuario()
            
# menu
while True:
    print("1 - ir para o programa")
    print("2 - sair")
    escolhaU = int(input("Insira um valor: "))
    opcaoPrograma = 1
    opcaoSair = 2
    if(escolhaU == opcaoPrograma):
        print("Indo para o programa...")
        main()
    elif(escolhaU == opcaoSair):
        print("Saindo...")
        break
    else:
        print("Valor incorreto. Insira novamente.")