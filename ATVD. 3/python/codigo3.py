nomeUsuario = input("Insira o seu nome: ")
ocupacaoUsuario = input("Insira o seu cargo/ocupação: ")

def saudacao(nome, tituloProfissional):
    return (f"Olá, {tituloProfissional} {nome} !")

saudacaoProfissional = saudacao(nomeUsuario, ocupacaoUsuario)
print(saudacaoProfissional)