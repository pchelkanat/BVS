from math import gcd
from random import random

from prog.EGCD import egcd
from prog.MRPT import MillerRabin

def modInverse(e,n):
    return egcd(e,n)[0]%n


def getPrime(bits=512):
    n = 1
    while not MillerRabin(n,5):
        n = random.getrandbits(bits)
    return n


def generateKeys(nbits=1024):
    p = getPrime(512)
    q = getPrime(512)
    print("primes:", p, q)
    n = p * q
    # phi=EulerPhi(n)
    phi = (p - 1) * (q - 1)

    # public=(e,n)
    # private= d, тчо НОД(d,n)=1
    good_d = False
    while not good_d:
        d = random.getrandbits(nbits // 4)
        if gcd(d, phi) == 1:
            good_d = True

    # подразумеваем, что умеем находить обратный элемент по модулю
    e = modInverse(d, phi)
    return e, n, d

#кодируем
def encoding(m):
    e, n, d = generateKeys()
    m_cod = (m**e)%n #powmod(m, e, n)
    print(e, n)
    return m_cod

#декодируем
def decording(m_cod):
    e, n, d = generateKeys()
    m_encod = (m_cod**d)%n #powmod(m_cod, d, n)
    print(d)
    return m_encod
