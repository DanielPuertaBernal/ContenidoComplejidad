def mcd(a, b):
    """
    Algoritmo de Euclides recursivo para calcular el MCD de dos números enteros.

    Parámetros:
        a (int): Primer número.
        b (int): Segundo número.

    Retorna:
        int: El máximo común divisor de a y b.
    """
    if b == 0:
        return a
    else:
        return mcd(b, a % b)

def mcd_iterativo(a, b):
    """
    Algoritmo de Euclides iterativo para calcular el MCD de dos números enteros.

    Parámetros:
        a (int): Primer número.
        b (int): Segundo número.

    Retorna:
        int: El máximo común divisor de a y b.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Ejemplo de uso
if __name__ == "__main__":
    x, y = map(int, input().split())
    print(f"El MCD de {x} y {y} es: {mcd(x, y)}")
    print(f"El MCD de {x} y {y} es: {mcd_iterativo(x, y)}")
