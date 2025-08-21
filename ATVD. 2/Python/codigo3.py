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

