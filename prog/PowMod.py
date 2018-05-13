def powmod(a, b, n):
    b = list(format(b, "b"))
    # print(b, type(b), len(b), type(int(b[0])))
    ar = [a]

    for i in range(len(b) - 1):
        if int(b[i + 1]) == 1:
            ar.append((a * ar[i] * ar[i]) % n)
        else:
            ar.append((ar[i] * ar[i]) % n)
    # print(ar, type(ar))
    return b, ar, ar[len(ar) - 1]

# print(powmod(2, 50, 21))
# print(powmod(3, 145, 45))
# print(powmod(2, 100, 27))
# print(powmod(3, 200, 55))