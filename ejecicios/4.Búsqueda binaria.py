def binary_search(arr, target):
    """
    Búsqueda binaria

    Descripción del problema:
        Dado un arreglo ordenado ascendentemente 'arr' y un valor 'target', determinar si 'target'
        existe en 'arr'. Si existe, retornar el índice de una ocurrencia. Si no existe, retornar -1.

    Solución:
        1. Mantener dos punteros: left = 0, right = len(arr) - 1.
        2. Mientras left <= right:
            a. Calcular mid = (left + right) // 2.
            b. Si arr[mid] == target, retornar mid.
            c. Si arr[mid] < target, significa que target solo puede estar en la porción derecha:
                 left = mid + 1
            d. Si arr[mid] > target, target solo puede estar en la porción izquierda:
                 right = mid - 1
        3. Si salimos del ciclo sin encontrar target, retornar -1.

    Consideraciones:
        - El arreglo debe estar previamente ordenado de forma ascendente para que funcione correctamente.
        - Puede adaptarse fácilmente a búsqueda en orden descendente modificando las comparaciones.

    """
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Ejemplo de uso:
if __name__ == "__main__":
    lista_ordenada = [1, 3, 5, 7, 9, 11]
    objetivo = 7
    indice = binary_search(lista_ordenada, objetivo)
    if indice != -1:
        print(f"Elemento {objetivo} encontrado en índice {indice}")
    else:
        print(f"Elemento {objetivo} no encontrado en la lista ordenada")
