# Crie um programa que:

# Peça o nome de usuário e senha até que sejam informados corretamente.
# Considere como válidos: usuário "admin" e senha "1234".
# Após o login, pergunte a idade e diga se o acesso é completo (idade ≥ 18) ou restrito.
# Utilize estrutura de repetição e operadores lógicos.

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
