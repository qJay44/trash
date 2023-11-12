ALPHABET_LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13(input: str):
    output = ""
    for char in input:
        if char not in ALPHABET_UPPERCASE and char not in ALPHABET_LOWERCASE:
            output += char
        elif char.isupper():
            output += ALPHABET_UPPERCASE[(ALPHABET_UPPERCASE.find(char) + 13) % len(ALPHABET_UPPERCASE)]
        else:
            output += ALPHABET_LOWERCASE[(ALPHABET_LOWERCASE.find(char) + 13) % len(ALPHABET_LOWERCASE)]

    print(output)


print("string:")
rot13(str(input()))

