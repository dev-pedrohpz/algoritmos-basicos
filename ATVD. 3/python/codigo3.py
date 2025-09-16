# Implemente um sistema de senha com máximo de 3 tentativas.
# A senha correta é Acesso@4321.
# O programa deve permitir até 3 tentativas.

# Se acertar, exiba: "Acesso concedido"
# Se errar todas, exiba: "Acesso bloqueado"
# Use uma função para verificar a senha.

# PS: Se fizer em Java, a comparação de igualdade de string deve ser feita com a função nativa equals. 
# Exemplo: senha_correta.equals(senha_usuario);


senhaAcesso = "Acesso@4321"

def verificacaoSenha():
    print("Sistema de Verificação")
    situacao = ""
    for i in range(1, 4):
        senha = input("Insira a senha: ")
        if(senha == senhaAcesso):
            situacao = print("Acesso concedido!")
            break
        elif(senha != senhaAcesso):
            situacao = print("Acesso bloqueado.")
            if(i == 3):
                print("Suas chances encerraram.")
            else:
                print(f"Tem direito a {i}/3")
            
            
    return situacao

verificacaoSenha() ## por ser uma função que não recebe parâmetros, precisa ser chamada

