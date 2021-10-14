def conversor(razon_de_cambio, monto):
    monto = monto / razon_de_cambio
    monto = str(round(monto, 2))
    return monto


def main():
    menu = """
    Bienvenido, este es un conversor de monedas.
    Elige una de las siguiente opciones:
    1- Pesos Mexicano a Dolares Estadounidenses (MXN/USD)
    2- Dolares Estadounidenses a Pesos Mexicanos (USD/MXN)
    """
    opcion = input(menu)
    if opcion == "1":
        pesos_mexicanos = float(input("¿Cuántos pesos mexicanos(MXN) tienes?: "))
        dolares = conversor(20.75, pesos_mexicanos)
        print("Los pesos mexicanos que tienes equivalen a $" + dolares + " USD")
    elif opcion == "2":
        usd = float(input("¿Cuántos dólares estadounidenses(USD) tienes?: "))
        mxn = conversor(0.4, usd)
        print("Los dólares estadounidenses que tienes equivalen a $" + mxn + " MXN")


if __name__ == "__main__":
    main()
