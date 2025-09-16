# Peça ao usuário dois números que representem o início e o fim de um intervalo.
# Depois, peça outro número que será o divisor.
# O programa deve mostrar todos os múltiplos do divisor dentro do intervalo informado.

# Exemplo:
# Início: 10
# Fim: 30
# Divisor: 4
# Saída: 12, 16, 20, 24, 28

valor1 = int(input("Insira o valor do ínicio: "))
valor2 = int(input("Insira o valor do fim: "))
divisor = int(input("Insira o divisor: "))
valorInicial = valor1 #armazena o valor inicial nessa variável, antes da primeir começar a ser modificada
multiplos = []

while valor1 <= valor2:
    if( valor1 %divisor == 0):
        multiplos.append(valor1)
    valor1 = valor1 + 1    

print(f"O valor de ínicio é: {valorInicial}")    
print(f"O valor de fim é: {valor2}")  
print(f"O divisor que percorrerá esse intervalo: {divisor}")
print(f"OS multíplos presentes nesse intervalo do divisor {divisor} são: {multiplos}")