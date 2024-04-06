
n = int(input("Insira a quantidade de temperaturas: "))
cont = 1

while cont <= n:
    c = float(input("Insira a temperatura em celsius: "))
    farenheit = (9 / 5) * c + 32 
    kelvin = c + 273
    reaumur =  c * (4 / 5) 
    print(f"Temperatura em farenheit = {farenheit :.1f}\nemperatura em kelvin = {kelvin :.1f}\nTemperatura em reaumur = {reaumur :.1f}")


    cont = cont + 1