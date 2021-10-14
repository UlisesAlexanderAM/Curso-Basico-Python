def conversor(razon_de_cambio, monto):
    monto = monto / razon_de_cambio
    monto = str(round(monto, 2))
    return monto


menu = """
Bienvenido, este es un conversor de monedas.
Elige una de las siguiente opciones:
1- Pesos Mexicano a Dolares Estadounidenses (MXN/USD)
2- Dolares Estadounidenses a Pesos Mexicanos (USD/MXN)
 """
opcion = input(menu)
if opcion == "1":
    pesos_mexicanos = input("¿Cuántos pesos mexicanos(MXN) tienes?: ")
    pesos_mexicanos = float(pesos_mexicanos)
    conversor(20.75, pesos_mexicanos)
    print("Los pesos mexicanos que tienes equivalen a $" + dolares + " USD")
elif opcion == "2":
    usd = input("¿Cuántos dólares estadounidenses(USD) tienes?: ")
    usd = float(usd)
    conversor(0.4, usd)
    print("Los dólares estadounidenses que tienes equivalen a $" + mxn + " MXN")
