# Crie uma função que recebe um ano e retorna se ele é bissexto.

# Um ano é bissexto se for divisível por 4, exceto os múltiplos de 100, a menos que também sejam divisíveis por 400.

# Exemplo:

2000 → bissexto

1900 → não bissexto

2024 → bissexto

def main():

    anoAnalisado = int(input("Insira um ano: "))

    def verificadorAnoBissexto(ano):
        anoBissexto = ano %400 == 0
        anoBissextoAlt = ano %4 == 0 and ano%100 !=0
        situacao = ""
        if(anoBissexto or anoBissextoAlt):
            situacao = "Bissexto"
        else:
            situacao = "Não é bissexto."
        
        return situacao

    print(verificadorAnoBissexto(anoAnalisado))
        
main()