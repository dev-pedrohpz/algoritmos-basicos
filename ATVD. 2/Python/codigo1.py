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