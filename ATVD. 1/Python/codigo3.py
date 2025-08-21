votantesAptos = []
votantesN_Aptos = []
pessoas = []

for i in range (0, 5):
    pessoa = input("Digite o nome do cidadão: ")
    pessoas.append(pessoa)

    idade = int(input("Digite a idade do cidadão: "))

    idadeApta = idade >= 18
    idadeN_Apta = idade < 18

    if(idadeApta == True):
        print("Está apto!")
        votantesAptos.append(pessoa)

    elif(idadeN_Apta == True):
        print("Não está apto!")
        votantesN_Aptos.append(pessoa)   

print(F"Do grupo {pessoas}, os aptos são {votantesAptos} e os não aptos: {votantesN_Aptos}" ) 

# // posso criar uma variável que armazene a relação de qual array é maior ao invés de escrever na condicional

if(len(votantesAptos) > len(votantesN_Aptos)):
    print("A maioria esta apta para votar.")

elif(len(votantesN_Aptos) > len(votantesAptos)):
    print("A maioria não está apta para votar.")  

else:
    print("Deu empate!")      


