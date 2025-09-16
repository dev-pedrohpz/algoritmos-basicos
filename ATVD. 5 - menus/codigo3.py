# Implemente funções para conversões:
# Celsius ↔ Fahrenheit
# Metros ↔ Quilômetros
# Horas ↔ Minutos
# Depois crie um menu principal que permite escolher a conversão e reaproveite as funções criadas.

def main():

    # função principal para conversão de temperatura

    def conversaoTemp(tempCelsius, tempFahre):

        opcaoC = 1

        opcaoF = 2

        situacao = ""

        print("1 - Celsius para Fahrenheit ")

        print("2 - Fahrenheit para Celsius ")

        escolhaT = int(input("Insira o número da conversão que deseja: "))


        if (escolhaT == opcaoC):

            tempF = tempCelsius * 1.38 + 32

            situacao = tempF

            return situacao

        elif (escolhaT == opcaoF):

            tempC = (tempFahre - 32) * 1.38

            situacao = tempC

            return situacao

 

    def conversaoDistancia(valorMetros, valorKm):

        opcaoM = 1

        opcaoKm = 2

        situacao = ""

        print("1 - Metros para Km ")

        print("2 - Km para Metros ")

        escolhaD = int(input("Insira o número da conversão que deseja: "))

 
        if (escolhaD == opcaoM):

            distanciaConvertida = valorMetros / 1000

            situacao = distanciaConvertida

            return situacao

        elif (escolhaD == opcaoKm):

            distanciaConvertida = valorKm * 1000

            situacao = distanciaConvertida

            return situacao


    def conversaoTempo(valorHora, valorMinuto):

        opcaoH = 1

        opcaoMin = 2

        situacao = ""

        print("1 - Horas para Minuto ")

        print("2 - Minutos para Hora ")

        escolhaD = int(input("Insira o número da conversão que deseja: "))


        if (escolhaD == opcaoH):

            tempoConvertido = valorHora * 60

            situacao = tempoConvertido

            return situacao

        elif (escolhaD == opcaoMin):

            tempoConvertido = valorMinuto / 60

            situacao = tempoConvertido

            return situacao


    # função sem parÂmetro e que permite o usuário escolher qual operação quer realizar, chamando outras funçõe.

    def escolhaUsuario():

        print("1 - Conversão de Temperaturas")

        print("2 - Conversão de Distância")

        print("3 - Conversão de Tempo")

        cTemper = 1

        cDist = 2

        cTempo = 3

        situacao = ""

        opcao = int(input("Insira qual ação deseja realizar: "))

        if (opcao == cTemper):

            escolhaTemp()

        elif (opcao == cDist):

            escolhaDist()

        elif (opcao == cTempo):

            escolhaTempo()

        else:

            print("valor incorreto.")

            escolhaUsuario()

 

    # função chamada caso a escolha do usuario seja a conversão de temperaturas, não recebe nenhum parâmetro, apenas imprime uma string e chama outras funcoes.

    def escolhaTemp():

        tempC = int(input("Insira a temperatura em Celsius: "))

        tempF = int(input("Insira a temperatura em Fahrenhait: "))

        conversao = conversaoTemp(tempC, tempF)

        print(f"O reultado da conversão escolhida é: {conversao}")




    def escolhaDist():

        distM = int(input("Insira o valor em metros: "))

        distKm = int(input("Insira o valor em Kms: "))

        conversao = conversaoDistancia(distM, distKm)

        print(f"O reultado da conversão escolhida é: {conversao}")




    def escolhaTempo():

        tempHora = int(input("Insira as horas: "))

        tempMinuto = int(input("Insira os minutos: "))

        conversao = conversaoTempo(tempHora, tempMinuto)

        print(f"O reultado da conversão escolhida é: {conversao}")

    escolhaUsuario()

 

# menu

 

while True:

    print("Bem vindo ao programa de Conversões!\n"

          "1 - Ir para o menu de Conversões\n"

          "2 - Sair")

    opcao1 = 1

    opcao2 = 2

    opcaoUsuario = int(input("Insira oque deseja fazer: "))

    if (opcaoUsuario == opcao1):

        print("\n"

              "Carregando...")

        main()

    elif (opcaoUsuario == opcao2):

        print("\n"

              "Saindo...")

    else:

        print("\n"

              "Valor incorreto.")