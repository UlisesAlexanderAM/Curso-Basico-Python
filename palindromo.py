def es_palindromo(palabra: str):
    palabra = palabra.replace(" ", "")
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def main():
    palabra = input("Escribe una palabra")
    if es_palindromo(palabra):
        print("Es palíndromo")
    else:
        print("No es palíndromo")


if __name__ == "__main__":
    main()
