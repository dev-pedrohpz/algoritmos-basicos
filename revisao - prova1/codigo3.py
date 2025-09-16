numeros = []
def main():
    def leituraNumeros():
        qntsNumeros = int(input("Insira a quantidade de números que deseja: "))
        for i in range(0, qntsNumeros):
            valor = int(input(f"Insira o {i +1} valor: "))
            numeros.append(valor)
        
    def calculoMaiorValor():
        maiorValor = max(numeros)
        return maiorValor
        
    def calculoMenorValor():
        menorValor = min(numeros)
        return menorValor

    def exibirResultados():
        quantidadeNumeros = numeros
        maiorValor = calculoMaiorValor()
        menorValor = calculoMenorValor()
        print("Os resultados são esses: ")
        print(f"Valores: {numeros}")
        print(f"Maior valor: {maiorValor}")
        print(f"Menor valor: {menorValor}")
        
    leituraNumeros()
    exibirResultados()
        
main()