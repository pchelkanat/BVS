import itertools as it

def gengamma():
    gamma=[]
    return gamma

def encryptGamma(text, gamma):
    code=[]
    for i,j in it.izip(text, it.cycle(gamma)):
        code.append(chr(ord(i)^ord(j)))
    return ''.join(code)

def decryptGamma(code, gamma):
    text=[]
    for i, j in it.izip(code, it.cycle(gamma)):
        text.append(chr(ord(i)^ord(j)))

    return ''.join(text)