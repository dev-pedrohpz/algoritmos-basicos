# Crie uma função que receba dois parâmetros: um nome e um título profissional (por exemplo, “Engenheiro(a)”).
# A função deve retornar uma string formatada no padrão: "Olá, [Título] [Nome]!".
# Exiba o resultado no programa principal.

nomeUsuario = input("Insira o seu nome: ")
ocupacaoUsuario = input("Insira o seu cargo/ocupação: ")

def saudacao(nome, tituloProfissional):
    return (f"Olá, {tituloProfissional} {nome} !")

saudacaoProfissional = saudacao(nomeUsuario, ocupacaoUsuario)
print(saudacaoProfissional)