# Um sistema precisa processar vendas de produtos.
# calcular_total(qtd, preco) → retorna o valor total.
# aplicar_desconto(valor, percentual) → aplica desconto.
# exibir_resumo(nome, qtd, preco, desconto) → mostra os resultados.
# Reaproveite as funções para calcular o valor de 3 produtos diferentes.

def main():

    def calcularTotal(qntd, preco):

        valorTotal = qntd * preco

        return valorTotal

    def aplicarDesconto(valor, percentual):

        valorDesconto = valor * (percentual/100)

        valorTotal = valor - valorDesconto

        return valorTotal

    def exibirResumo(nome, qtd, preco, desconto):

        print("Resumo: ")

        print(f"Produto: {nome}")

        print(f"Quantidade: {qtd}")

        print(f"Preço: {preco}")

        print(f"Desconto: {desconto}")


    print("Insira as informações: ")

    nomeMercadoria = input("Insira o nome do produto: ")

    quantidade = int(input("Insira a quantidade: "))

    valorMercadoria = float(input("Insira o valor unitário: "))

    valorDesconto = int(input("Insira o valor de desconto: "))

    total = calcularTotal(quantidade, valorMercadoria)

    descontoCompra = aplicarDesconto(valorMercadoria, valorDesconto)

    resumo = exibirResumo(nomeMercadoria, quantidade, valorMercadoria, valorDesconto)

    print(f"O total é: {total}")

    print(f"O valor descontado é: {descontoCompra}")

    # print(resumo)

while True: # criação de menu em python

    print("1 - Ir para o programa de Compras")

    print("2 - Sair")

    programa = 1

    saida = 2

    escolha = int(input("Digita um valor: "))

    if(escolha == programa):

        main()

    elif(escolha == saida):

        print("saindo...")

        break

    else:

        print("Valor incorreto")