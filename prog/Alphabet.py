alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
            'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


###mod 33
def encryptVigenere(key, text):
    textLen = len(text)
    keyLen = len(key)

    # Формируем ключевое слово(растягиваем ключ на длину текста)
    keyText = []
    for i in range(textLen // keyLen):
        for symb in key:
            keyText.append(symb)
    for i in range(textLen % keyLen):
        keyText.append(key[i])

    # Шифрование
    code = []
    for i in range(textLen):
        code.append(alphabet[(alphabet.index(text[i]) + alphabet.index(keyText[i])) % 33])

    return ''.join(code)


def decryptVigenere(key, code):
    codeLen = len(code)
    keyLen = len(key)

    # Формируем ключевое слово(растягиваем ключ на длину текста)
    keyText = []
    for i in range(codeLen // keyLen):
        for symb in key:
            keyText.append(symb)
    for i in range(codeLen % keyLen):
        keyText.append(key[i])

    # Расшифровка
    text = []
    for i in range(codeLen):
        text.append(alphabet[(alphabet.index(code[i]) - alphabet.index(keyText[i]) + 33) % 33])

    return ''.join(text)


def encryptCaesar(key, text):
    print(key,type(key))
    key=int(key)%33
    print(key)
    code = []
    for i in range(len(text)):
        code.append(alphabet[(alphabet.index(text[i]) + key) % 33])

    return ''.join(code)


def decryptCaesar(key, code):
    print(key,type(key))
    key = int(key) % 33
    text = []
    for i in range(len(code)):
        text.append(alphabet[(alphabet.index(code[i]) - key) % 33])

    return ''.join(text)