
n = int(input("Insira o número de países: "))
cont = 1
total_comercial = 0
continente_europeu = 0
continente_africano = 0
continente_africano_comercial = 0

while cont <= n:

    continente = input("Insira o continente: ")
    balanca_comercial = float(input("Insira o valor da balança comercial: "))
    populacao = int(input("Insira o número da população: "))

    total_comercial = total_comercial + balanca_comercial
    
    if continente == "E" or continente == "e":
        continente_europeu = continente_europeu + 1

        if continente_europeu == 1:
            maior_populacao = populacao

        elif populacao > maior_populacao:
            maior_populacao = populacao

    if continente == "F" or continente == "f":
        continente_africano = continente_africano + 1

        if balanca_comercial < 100000000:
            continente_africano_comercial = continente_africano_comercial + 1


    cont = cont + 1

media_comercial = total_comercial / n
porcentagem_africano_comercial = continente_africano_comercial * 100 / continente_africano

print(f"Média da balança comercial = {media_comercial :.2f}\nMaior população entre os países da Europa = {maior_populacao}")
print(f"Porcentagem de países africanos com balança comercial inferior a 100 milhões = {porcentagem_africano_comercial :.2f}")