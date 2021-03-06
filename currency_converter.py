def converter(exchange_rate: float, amount: float) -> str:
    """Converts a currency to another currency

    param float exchange_rate the exchange rate between currencies
    param float amount the amount of money to convert
    returns the amount of money in the currency to convert
    """
    try:
        amount = amount / exchange_rate
        amount_string = str(round(amount, 2))
        return amount_string
    except ZeroDivisionError as e:
        return f"{e}. \nEl tipo de cambio {exchange_rate} es cero. Tipo de cambio invalido."


def main():
    menu = """
    Bienvenido, este es un conversor de monedas.
    Elige una de las siguiente opciones:
    1- Pesos Mexicano a Dólares Estadounidenses (MXN/USD)
    2- Dólares Estadounidenses a Pesos Mexicanos (USD/MXN)

    """

    option = input(menu)

    if option == "1":
        mexican_pesos = float(input("¿Cuántos pesos mexicanos(MXN) tienes?: "))
        dolares = converter(20.75, mexican_pesos)
        print("Los pesos mexicanos que tienes equivalen a $" + dolares + " USD")
    elif option == "2":
        usd = float(input("¿Cuántos dólares estadounidenses(USD) tienes?: "))
        mxn = converter(0.04, usd)
        print("Los dólares estadounidenses que tienes equivalen a $" + mxn + " MXN")
    else:
        print("Opción incorrecta")


if __name__ == "__main__":
    main()
