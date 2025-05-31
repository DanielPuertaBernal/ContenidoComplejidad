def bubble_sort(arr):
    """
    Ordenamiento por el método burbuja

    Descripción del problema:
        Dado un arreglo 'arr' de elementos comparables, queremos regresar el mismo arreglo
        ordenado en orden ascendente.

    Solución (burbuja clásica):
        1. Recorremos el arreglo varias pasadas.
        2. En cada pasada, comparamos elementos adyacentes arr[j] y arr[j + 1].
        3. Si arr[j] > arr[j + 1], intercambiamos dichos elementos.
        4. Cada pasada “burbujea” el elemento más grande restante hacia el final.
        5. Repetimos pasadas hasta que en una pasada no haya intercambios, lo que indica
           que el arreglo ya está ordenado (optimización).

    Pasos detallados:
        - length = len(arr)
        - Para i en rango(0, length):
            * bandera_swap = False  # Para detectar si hubo intercambios
            * Para j en rango(0, length - i - 1):
                - Si arr[j] > arr[j + 1]:
                    • Intercambiar arr[j] y arr[j + 1]
                    • bandera_swap = True
            * Si bandera_swap es False al terminar el bucle interno, terminar el algoritmo.

    Complejidad:
        - Mejor caso (arreglo ya ordenado, usamos optimización): O(n).
        - Peor caso y caso medio: O(n²), por la doble iteración.
    """
    n = len(arr)
    # Convertimos a lista si viene en otra forma de colección
    arr = list(arr)
    for i in range(n):
        swapped = False
        # En cada pasada, los últimos i elementos ya están ordenados
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Intercambiar elementos adyacentes
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Si no hubo intercambios en esta pasada, terminamos
        if not swapped:
            break
    return arr


# Ejemplo de uso:
if __name__ == "__main__":
    lista_desordenada = [64, 34, 25, 12, 22, 11, 90]
    lista_ordenada = bubble_sort(lista_desordenada)
    print("Lista original:", lista_desordenada)
    print("Lista ordenada  :", lista_ordenada)
