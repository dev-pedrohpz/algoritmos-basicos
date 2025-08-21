n1 = float(input("Insira a N1: "))
n2 = float(input("Insira a N2: "))
n3 = float(input("Insira a N3: "))

def mediaNotas(nota1, nota2, nota3):
    media = (nota1+nota2+nota3)/3
    return media

mediaAluno = mediaNotas(n1, n2, n3)

aprovado = mediaAluno >= 7
situacao = ""

if(aprovado):
    situacao = "Aprovado!"
elif(not aprovado):
    situacao = "Reprovado!"    

print(f"Sua média é de {mediaAluno:,.2f} , está {situacao}")