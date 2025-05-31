import time


def factorial_iterative(n: int) -> int:
    """
    Factorial Iterativo

    El factorial de un número entero no negativo n (n!) se define como:
        n! = 1 * 2 * 3 * ... * n, para n >= 1
        0! = 1 (definición especial)

    Dado n >= 0, retorna n!.
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


def factorial_recursive(n: int) -> int:
    """
    Factorial Recursivo

    Similar a la versión iterativa, pero usando recursión:
        n! = n * (n-1)! para n >= 1
        0! = 1
    """
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos.")

    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == "__main__":
    # Puedes ajustar este valor para probar números más grandes o más pequeños
    valor_n_prueba = 5

    # --- Medir tiempo para la función factorial_iterative ---
    tiempo_i_inicio = time.time()
    resultado_iterativo = factorial_iterative(valor_n_prueba)
    tiempo_i_fin = time.time()
    tiempo_i = tiempo_i_fin - tiempo_i_inicio
    print(f"Factorial iterativo de {valor_n_prueba}: {resultado_iterativo}")
    print(f"Tiempo de ejecución iterativo: {tiempo_i:.6f} segundos")

    # --- Medir tiempo para la función factorial_recursive ---
    tiempo_r_inicio = time.time()
    resultado_recursivo = factorial_recursive(valor_n_prueba)
    tiempo_r_fin = time.time()
    tiempo_r = tiempo_r_fin - tiempo_r_inicio
    print(f"Factorial recursivo de {valor_n_prueba}: {resultado_recursivo}")
    print(f"Tiempo de ejecución recursivo: {tiempo_r:.6f} segundos")