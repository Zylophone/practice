def hilbert_curve(x, y, iter):
    if iter <= 0:
        return 1
    length = 1 << (iter - 1)
    num = 1 << (2 * (iter - 1))
    if x >= length and y >= length:
        return 2 * num + hilbert_curve(x - length, y - length, iter - 1)
    elif x < length and y >= length:
        return num + hilbert_curve(x, y - length, iter - 1)
    elif x < length and y < length:
        return hilbert_curve(y, x, iter - 1)
    else:
        return hilbert_curve(length - y - 1, length - x - 1, iter - 1)


print hilbert_curve(2, 2, 2)
print hilbert_curve(0, 1, 2)
print hilbert_curve(2, 3, 2)
