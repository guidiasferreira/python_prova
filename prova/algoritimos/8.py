
n = int(input("Insira o inicial: "))
m = int(input("Insira o final: "))

produto = 1

while n <= m:
    if n % 2 == 0:
        produto = produto * n
        print(f"Produto = {produto}")


    n = n + 1 