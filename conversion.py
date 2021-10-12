#!/usr/bin/env python3

pesos_mexicanos = input("¿Cuantos pesos mexicanos(MXN) tienes?: ")
pesos_mexicanos = float(pesos_mexicanos)
valor_dolar = 20.75
dolares = pesos_mexicanos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)

usd = input("¿Cuantos dolares estadounidenses(USD) tienes?: ")
usd = float(usd)
valor_mxn = 0.04
mxn = usd / valor_mxn
mxn = round(mxn, 2)
mxn = str(mxn)

print("Los pesos mexicanos que tienes equivalen a $" + dolares + " USD")
print("Los dolares estadounidenses que tienes equivalen a $" + mxn + " MXN")
