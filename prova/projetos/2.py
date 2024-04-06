
n = int(input("Insira os dados de N pessoas: "))
cont = 1
total_lanche = 0

while cont <= n:
    tipo_lanche = input(f"Insira o tipo de lanche da {cont}\u00AA pessoa: ")
    quantidade = int(input(f"Insira a quantidade de lanche da {cont}\u00AA pessoa: "))

    if tipo_lanche == "hamburguer":
        valor = 20

    elif tipo_lanche == "xburguer":
        valor = 25

    elif tipo_lanche == "hot_dog":
        valor = 30

    else:
        valor = 40

    total_lanche = valor * quantidade
    print(f"Você irá pagar um total de {total_lanche :.2f} reais")

    cont = cont + 1