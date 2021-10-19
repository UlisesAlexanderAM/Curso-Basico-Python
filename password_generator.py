import random


def characters_list():
    """Create a list of character from 4 separates list (MAYUS,MINUS,NUMS,CHARS).

    returns a list o characters
    """

    MAYUS = [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "Ñ",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "X",
        "Y",
        "Z",
    ]
    MINUS = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "ñ",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "x",
        "y",
        "z",
    ]
    NUMS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    CHARS = [
        "*",
        "+",
        "-",
        "/",
        "@",
        "_",
        "¿",
        "?",
        "!",
        "[",
        "{",
        "(",
        ")",
        "}",
        "]",
        ",",
        ";",
        ".",
        ">",
        "<",
        "~",
        "°",
        "^",
        "&",
        "$",
        "#",
        '"',
    ]

    characters = MAYUS + MINUS + NUMS + CHARS
    return characters


def generate_password(chars):
    """Generates a random password.

    param list(str) chars
    returns a random password
    """

    password = []
    for i in range(15):
        random_char = random.choice(chars)
        password.append(random_char)
    password = "".join(password)
    return password


def main():
    chars = characters_list()
    password = generate_password(chars)
    print(password)


if __name__ == "__main__":
    main()
