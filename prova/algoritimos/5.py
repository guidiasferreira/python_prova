
n = int(input("Insira o número para calcular o fatorial: "))
cont = 1
fatorial = 1

while cont <= n:
    fatorial = fatorial * cont 
  
    if n >= 0:
        print(f"O fatorial de {cont} é {fatorial}")

    else:
        print(f"Não existe fatorial de número negativo!")


    cont = cont + 1
