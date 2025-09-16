nomes = []
def main():
    def cadastroNomes():
        qntdNomes = int(input("Insira a quantidade de números que deseja cadastrar: "))
        for i in range(0, qntdNomes):
            nome = input(f"Insira o {i + 1} nome: ")
            nomes.append(nome)
            print(f"{nome} inserido!")
            
    def verificarLista():
        print("Verificação de nomes cadastrados!!!")
        nome = input("Insira o nome: ")
        nomeInserido = nome in nomes
        if(nomeInserido):
            print(f"O nome {nome} está na lista.")
        else:
            print(f"O nome {nome} não está na lista.")
            
    cadastroNomes()
    verificarLista()
    
main()