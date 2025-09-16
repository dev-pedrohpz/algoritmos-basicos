# Crie um programa modularizado que receba um número inteiro e retorne se ele é par ou ímpar. 
# A função deve retornar um valor booleano 
# e outro procedimento deve imprimir a mensagem apropriada com base nesse valor.

valor = int(input(“Insira 1 valor: “))
numero = valor
situacao = “”

def verificacaoNumero(numero):
    numeroPar = numero %2 == 0
    return numeroPar

resultado = verificacaoNumero       

def valorVerificado(booleano)
    if(numeroPar):
        situacao = “Par”
    else:
        situacao = “Ímpar” 
        
    print (“seu número é “ + situacao)

print(valorVerificado(resultado))