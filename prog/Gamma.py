from itertools import cycle


def encryptGamma(text, gamma):
    code = []
    # print(str(text),str(code),str(gamma))
    for i, j in zip(text, cycle(gamma)):
        # print(ord(i),ord(j),ord(i) ^ ord(j))
        code.append(chr(ord(i) ^ ord(j)))
        # print(code)
    return ''.join(code)


def decryptGamma(code, gamma):
    text = []
    # print(str(text), str(code), str(gamma))
    for i, j in zip(code, cycle(gamma)):
        # print(ord(i),ord(j),ord(i)^ord(j))
        text.append(chr(ord(i) ^ ord(j)))
        # print(text)

    return ''.join(text)


    # print(encryptGamma("нввфыап","ssdd"))
    # print(chr(23),chr(2), 100^115)
