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


def MillerRabin(n):
    # простые числа < 6 принимаются за составные, поэтому определим их

    if n < 6:
        return [False, False, True, True, False, True][n]
    elif n & 1 == 0:
        return False

    # число свидетелей простоты
    #countOfWitnesses = 0
    s, t = checkN(n)
    # print(s, d)
    for a in range(2, n-1):
        b = (a ** t) % n
        if b == 1 or b == (n - 1):
            #countOfWitnesses += 1
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
    #print(countOfWitnesses)
    return True # Простое


# print(-1 % 10)
# print(checkN(2), checkN(9))
#print(MillerRabin(149), MillerRabin(113))
