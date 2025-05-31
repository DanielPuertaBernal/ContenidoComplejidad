import time

def fibonacci_iterative(n):
    """
    Fibonacci Iterativo

    Descripción del problema:
        La serie de Fibonacci se define como:
            F(0) = 0
            F(1) = 1
            F(n) = F(n-1) + F(n-2) para n >= 2
        Queremos calcular F(n).

    Solución iterativa:
        1. Si n < 0: valor inválido, lanzar excepción.
        2. Si n == 0: retornar 0.
        3. Si n == 1: retornar 1.
        4. Inicializar dos variables: a = 0 (F(0)), b = 1 (F(1)).
        5. Iterar i desde 2 hasta n (inclusive):
            - c = a + b  # F(i)
            - a = b
            - b = c
        6. Al finalizar, b contendrá F(n).

    Complejidad:
        - Tiempo: O(n)
        - Espacio: O(1)
    """
    if n < 0:
        raise ValueError("El índice n debe ser no negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


def fibonacci_recursive(n):
    """
    Fibonacci Recursivo

    Descripción del problema:
        Similar al caso iterativo, calcular F(n) usando recursión directa:
            F(0) = 0
            F(1) = 1
            F(n) = F(n-1) + F(n-2)

    Solución recursiva (sin memoización):
        1. Si n < 0: excepción.
        2. Si n == 0: retornar 0.
        3. Si n == 1: retornar 1.
        4. Retornar fibonacci_recursive(n-1) + fibonacci_recursive(n-2).

    Consideraciones de complejidad:
        - Tiempo: O(2^n) en el peor caso (crecimiento exponencial), debido a solapamiento de subproblemas.
        - Espacio: O(n) por la profundidad máxima de la pila de recursión.
        - Para n grande, se vuelve ineficiente. Se recomienda memoización o versión iterativa.
    """
    if n < 0:
        raise ValueError("El índice n debe ser no negativo.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


# Ejemplo de uso:
if __name__ == "__main__":
    valor_n = 30  # Puedes cambiar este valor para probar diferentes 'n'

    # Medir tiempo para la función recursiva
    tiempo_r_inicio = time.time()
    resultado_r = fibonacci_recursive(valor_n)
    tiempo_r_fin = time.time()
    tiempo_r = tiempo_r_fin - tiempo_r_inicio
    print(f"Fibonacci recursivo de {valor_n}: {resultado_r}")
    print(f"Tiempo de ejecución recursivo: {tiempo_r:.6f} segundos")

    # Medir tiempo para la función iterativa
    tiempo_i_inicio = time.time()
    resultado_i = fibonacci_iterative(valor_n)
    tiempo_i_fin = time.time()
    tiempo_i = tiempo_i_fin - tiempo_i_inicio
    print(f"Fibonacci iterativo de {valor_n}: {resultado_i}")
    print(f"Tiempo de ejecución iterativo: {tiempo_i:.6f} segundos")