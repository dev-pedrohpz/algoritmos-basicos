# Peça o valor de uma compra e a forma de pagamento:

# 1 para à vista (10% de desconto)
# 2 para parcelado (sem desconto)
# Crie funções para calcular o valor final com base na escolha do usuário.
# Se parcelado, pergunte o número de parcelas e mostre o valor de cada uma.

valorCompra = float(input("Informe o valor da compra: "))
formaPagto = input("Informe a forma de pagamento (1 - à vista || 2 - à prazo) : ")

# numero = formaPagto
desconto = "1"
prazo = "2"
situacao = ""

def escolhaPagamento(numero):
    if(numero == desconto):
        situacao = pagtoVista()
    elif(numero == prazo):
        situacao = pagtoPrazo()
    else:
        print("Valor incorreto. Insira novamente.")
        
    return situacao
    
        
    
def pagtoPrazo():
     qntdParcelas = int(input("Informe a quantida de parcelas: "))
     valorParcelado = valorCompra / qntdParcelas
     situacao = (f"O valor da sua compra é de R${valorCompra}, dividido em {qntdParcelas}. \n O valor de cada parcela é de R${valorParcelado:,.2f}")
     return situacao

def pagtoVista():
    desconto = valorCompra * 0.10
    novoValor = valorCompra - desconto
    situacao = (f"O valor da sua compra é de R${valorCompra}, com o desconto aplicado o valor fica: R${novoValor}")
    return situacao


print(escolhaPagamento(formaPagto))
