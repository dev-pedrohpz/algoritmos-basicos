nome = input("Insira o seu nome: ")
idade = int(input("Insira a sua idade: "))
peso = float(input("Insira o seu peso: "))
altura = float(input("Insira a sua altura: "))

imc = peso/(altura * altura)
print(F"Seu IMC {nome}, é de: {imc:.2F}")

# maiorDeIdade = (idade >= 18 && idade < 60) -- "&&" não existe em python, e usa "and"

adulto = (idade >= 18 and idade < 60)
menorDeIdade = (idade < 18) 
idoso = (idade >= 60)
situacao = ""
alerta = ""

if(adulto == True):
    situacao = "adulto"
    if(imc > 25):
        alerta = "Atenção com a saúde"
    else:
        alerta = ""    
elif(menorDeIdade == True):
    situacao = "menor de idade"
    alerta = ""
elif(idoso == True):
    situacao = "idoso"
    alerta = ""

print(F"{nome}, seu IMC é de {imc:.2F}. {alerta}")    


