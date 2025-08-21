usuarioValido = "admin"
senhaValida = "1234"

usuario = input("Insira o usuário: ")
senha = input("Insira a senha: ")

while(usuario != usuarioValido and senha != senhaValida):
    usuario = input("Insira o usuário: ")
    senha = input("Insira a senha: ")

idade = int(input("Qual sua idade?: "))    
cadastroCompleto = idade >= 18
if(cadastroCompleto == True):
    print("Seu acesso é completo.")

else:
    print("Seu acesso é restrito.")

# posso dar uma refinada nesse código! Orgaiza-lo melhor.
