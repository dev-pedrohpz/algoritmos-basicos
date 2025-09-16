def mdc(a, b):
    if(b == 0):
        print(f"O mdc é {a}")
        return a
    else:
        print(a, b)
        return mdc(b, a % b)
        
valorA = int(input("Insira o primeiro valor: "))
valorB = int(input("Insira o segundo valor: "))
divisorComum = mdc(valorA, valorB)

print(f"O mdc de {valorA} e {valorB} é {divisorComum}")