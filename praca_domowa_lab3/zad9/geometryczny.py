def stworz_ciag(a1, q, n):
    lista = [a1 * (q ** x) for x in range(0, n + 1)]
    return lista


def suma_elementow(a1, q, n):
    suma = 0
    for x in range(0, n + 1):
        suma += a1 * (q ** x)
    return
