from math import gcd


def checkN(n):
    s = 0
    t = n - 1
    if n % 2 == 0 and n != 2:
        return False
    else:
        while t % 2 == 0:
            s = s + 1
            t = t / 2
    return s, int(t)


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


# print(EulerPhi(4),EulerPhi(2),EulerPhi(6))


def isWitness(s, t, n):
    num = int(EulerPhi(n) / 4)
    for a in range(2, num + 1):
        b = a ** t % n
        if b == 1:
            return True
        elif b == 0:
            for i in range(s):
                if b ** (2 ** i) % n == (-1 % n):
                    return True
                else:
                    return False
        else:
            return False


def MillerRabin(n, r=13):
    # простые числа < 6 принимаются за составные, поэтому определим их
    """
    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:
        return False
    """

    # число свидетелей простоты
    countOfWitnesses = 0
    s, t = checkN(n)
    # print(s, d)
    for a in range(2, r + 2):
        b = (a ** t) % n
        if b == 1 or b == (n - 1):
            countOfWitnesses += 1
            continue
        for i in range(s):
            b = (b ** 2) % n
            if b == 1:
                return False  # Составное
            elif b == (n - 1):
                a = 0
                break
        if a:
            return False
    print(countOfWitnesses)
    return countOfWitnesses, True # Простое


# print(-1 % 10)
# print(checkN(2), checkN(9))
print(MillerRabin(149), MillerRabin(1105))
