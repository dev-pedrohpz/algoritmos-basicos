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