def mediaValores(numero1, numero2, numero3):
    media = (numero1+numero2+numero3)/3
    return media #media é uma variável local, existente somente na função
    
valor1 = int(input("Insira o primeiro valor: "))  #variável global
valor2 = int(input("Insira o segundo valor: "))   #variável global
valor3 = int(input("Insira o terceiro valor: "))  #variável global

valorMedia = mediaValores(valor1,valor2,valor3) #variável global
print(f"A média dos valores {valor1}, {valor2} e {valor3} é: {valorMedia}")