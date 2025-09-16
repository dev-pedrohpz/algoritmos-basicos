# Monte um programa com as seguintes funções:

# ler_notas() → recebe as notas de um aluno.
# calcular_media() → calcula a média.
# verificar_situacao() → retorna "Aprovado" ou "Reprovado".
# exibir_resultado() → mostra a situação.
# Organize para que seja possível informar quantos alunos desejar e adicione uma opção no menu para encerrar o programa.

def main():

    nomeAluno = input("Insira o nome do aluno: ")

    def lerNotas():

        nota1 = float(input("Insira a nota 1: "))

        nota2 = float(input("Insira a nota 2: "))

        nota3 = float(input("Insira a nota 3: "))

        return nota1, nota2, nota3

    n1, n2, n3 = lerNotas() #desempacotamento, salvando múltiplos valores em uma variável cada. Ao invés de armazenar em array.

    print(n1, n2, n3)

    def calcularMedia(nota1, nota2, nota3):

        mediaCalculo = nota1 + nota2 + nota3 / 3

        return mediaCalculo

    mediaNotas = calcularMedia(n1,n2,n3)

    print(f"A média das notas é de {mediaNotas:.2f}")

    def verificarSituacao(media):

        aprovado = 7

        situacao = ""

        if(media >= aprovado):

            situacao = "Aprovado!"

            aprovados.append(nomeAluno)

        elif(media >= 5 and media < 7):

            situacao = "Recuperação"

            recuperacao.append(nomeAluno)

        elif(media < 5):

            situacao = "Reproavado!"

            reprovado.append(nomeAluno)

        return situacao

    situacaoAluno = verificarSituacao(mediaNotas)

    def exibirResultado(situacao):

        print(f"O aluno {nomeAluno} está {situacao}, pois sua média é de {mediaNotas:.2f}")

    print(exibirResultado(situacaoAluno))


aprovados = []

reprovado = [] 

recuperacao = []

while True:

    print("1 - Ir para o programa de Calcular Notas")

    print("2 - Sair")

    escolha1 = 1

    escolha2 = 2

    escolhaUsuario = int(input("Insira um valor: "))

    if(escolhaUsuario == escolha1):

        quantidadeAlunos = int(input("Insira quantos alunos: "))

        for i in range(0, quantidadeAlunos):

            print("rodando o programa...")

            main()
            
        print(f"Alunos aprovados: {aprovados}")

        print(f"Alunos reprovados: {reprovado}")

        print(f"Alunos recuperacao: {recuperacao}")

    elif(escolhaUsuario == escolha2):

        print("Saindo..")

        break

    else:

        print("valor incorreto")