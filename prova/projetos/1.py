
n = int(input("Insira o número de funcionários: "))
cont = 1
mulher = 0
homem = 0
total_idade = 0

while cont <= n:
    idade = int(input("Insira a idade: "))
    altura = float(input("Insira a altura: "))
    sexo = input("Insira o sexo: ")

    if sexo == "M" or sexo == "m":
        mulher = mulher + 1
        total_idade = total_idade + idade

        if mulher == 1:
            maior_idade = idade

        elif idade > maior_idade:
            maior_idade = idade

    if sexo == "H" or sexo == "h":
        homem = homem + 1

        if homem == 1:
            menor_altura = altura

        elif altura < menor_altura:
            menor_altura = altura


    cont = cont + 1

media_idade = total_idade / mulher
print(f"Maior idade entre as mulheres = {maior_idade}\nMenor altura entre os homens = {menor_altura :.2f}\nMédia de idade entre as mulheres = {media_idade :.2f}")