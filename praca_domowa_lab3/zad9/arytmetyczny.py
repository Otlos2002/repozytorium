
def stworz_ciag(a1, r, n):
    lista = [a1 + r * x for x in range(0, n + 1)]
    return lista


def suma_elementow(a1, r, n):
    suma = 0
    for x in range(0, n + 1):
        suma += a1 + r * x
    return suma
