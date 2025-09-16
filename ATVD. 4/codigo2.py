# Crie uma função que receba como parâmetros o nome de um produto e a quantidade comprada.
# Dentro da função, utilize uma variável local para calcular o novo total em estoque (estoque inicial fixo de 50 unidades). 
# Retorne esse total e exiba-o no programa principal.

nomeProduto1 = input("Informe o nome do produto: ")
quantidadeDesejada = int(input("Informe a quantidade desejada: "))

def verificacaoEstoque(nomeProduto, quantidadeProduto):
    quantidadeDisponivel = 50
    return quantidadeDisponivel - quantidadeProduto

resultado = verificacaoEstoque(nomeProduto1, quantidadeDesejada)
print(f"O estoque final do produto {nomeProduto1} é de: {resultado}")