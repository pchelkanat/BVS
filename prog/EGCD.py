def egcd(a, b):

    x, x1 = 1, 0
    y, y1 = 0, 1
    while b:
        q = a // b
        x, x1 = x1, x - q * x1
        y, y1 = y1, y - q * y1
        a, b = b, a - q * b
    return x, y, a