import random
from math import gcd

from prog.EGCD import egcd
from prog.mr import isPrime

bits = 128
nbits = bits * 2


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
    while True:
        num = random.randrange(2 ** (bits - 1), 2 ** (bits))
        if isPrime(num):
            return num


def generateKeys(bits):
    p = getPrime(bits)
    q = getPrime(bits)
    while p == q:
        q = getPrime(bits)

    n = p * q
    phi = (p - 1) * (q - 1)
    print("primes, n:", p, q, n)
    print("phi", phi)

    # public=(e,n)
    # private= d, тчо НОД(d,n)=1
    good_d = False
    while not good_d:
        # e = getrandbits(2*bits // 3)
        e = random.randrange(2 ** (nbits // 3 - 1), 2 ** (nbits // 3))
        if gcd(e, phi) == 1:
            good_d = True

    d = modInverse(phi, e)
    print("e,n,d", e, n, d)
    print("gcd (d,n)", egcd(d, n))
    return e, n, d


# кодируем
def encoding(m):
    e, n, d = generateKeys(bits)  # (len(str(m)))
    m_cod = []
    for i in range(len(m)):
        temp = pow(ord(m[i]), e, n)
        m_cod.append(temp)
    print("m_cod", m_cod)
    return m_cod, e, n, d


# декодируем
def decoding(m_cod, n, d):
    m_encod = []
    for i in range(len(m_cod)):
        temp = pow(m_cod[i], d, n)
        #print("temp",temp)
        m_encod.append(chr(temp%120000))
    # print("d", d)
    return ''.join(m_encod)


# n = getrandbits(nbits)
# print(n)
"""
s = "akjoeit"
bin = []
for ch in s:
    bin.append(ord(ch))
print(bin)

m, e, n, d = encoding(s)
print("en", m, e, n, d)
dec = decoding(m, n, d)
print(dec)
"""
