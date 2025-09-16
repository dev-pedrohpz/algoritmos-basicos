def main():
    print("Contagem regressiva, ou devo dizer, recursiva?")
    
    def contagemRegressiva(numero):
        if(numero == 0):
            print(numero)
            print(f"Contagem regressiva finalizada!")
            
        else:
            print(numero)
            return contagemRegressiva(numero -1)
            
    pontoPartida = int(input("Insira o ponto de partida para iniciar a contagem regressiva: "))
    
    contagemRegressiva(pontoPartida)
    
main()