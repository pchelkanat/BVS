from math import gcd
from random import getrandbits

from prog.EGCD import egcd
from prog.MRPT import MillerRabin


def modInverse(phi, e):
    y = egcd(phi, e)[2] % phi
    # print("y1",y)
    if y < 0:
        y = y + phi
    # print("y",y)
    return y


def EulerPhi(n):
    result = 1
    if not n % 2:
        for x in range(3, n, 2):
            if gcd(x, n) == 1:
                result += 1
    else:
        for x in range(2, n):
            if gcd(x, n) == 1:
                result += 1
    return result


def getPrime(bits):
    n = 1
    while not MillerRabin(n):
        # n=randint(bits)
        n = getrandbits(bits)

    return n


def generateKeys(nbits):
    p = getPrime(8)
    q = getPrime(8)
    while p == q:
        q = getPrime(8)

    n = p * q
    phi = (p - 1) * (q - 1)

    # public=(e,n)
    # private= d, тчо НОД(d,n)=1
    good_d = False
    while not good_d:
        e = getrandbits(nbits // 3)
        # e = randint(0, n - 1)
        if gcd(e, phi) == 1:
            good_d = True

    d = modInverse(phi, e)
    #print("primes:", p, q)
    #print("phi", phi)
    #print("e,n,d", e, n, d)
    #print("gcd", egcd(d, n))
    return e, n, d


# кодируем
def encoding(m):
    e, n, d = generateKeys(len(m) * 8)  # (len(str(m)))
    m_cod = []
    for i in range(len(m)):
        m_cod.append(chr((ord(m[i]) ** e) % n))  # powmod(m, e, n)
    return ''.join(m_cod), e, n, d


# декодируем
def decoding(m_cod, n, d):
    m_encod = []
    for i in range(len(m_cod)):
        m_encod.append(chr((ord(m_cod[i]) ** d) % n))  # powmod(m_cod, d, n)
    # print("d", d)
    return ''.join(m_encod)


"""
s = "akjoeit"
bin = []
for ch in s:
    bin.append(ord(ch))
print(bin)

en, n, d = encoding(s)
print("en", en,e, n, d)
dec = decoding(en, n, d)
print(dec)
"""
