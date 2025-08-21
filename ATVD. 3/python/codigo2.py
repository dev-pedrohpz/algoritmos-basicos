nomeProduto1 = input("Informe o nome do produto: ")
quantidadeDesejada = int(input("Informe a quantidade: "))

def verificacaoEstoque(nomeProduto, quantidadeProduto):
    quantidadeDisponivel = 50
    return quantidadeDisponivel - quantidadeProduto

resultado = verificacaoEstoque(nomeProduto1, quantidadeDesejada)
print(f"O estoque final do produto {nomeProduto1} é de: {resultado}")