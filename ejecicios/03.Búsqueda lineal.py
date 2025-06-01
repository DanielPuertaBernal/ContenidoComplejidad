def linear_search(arr, target):
    """
    Búsqueda lineal

    Descripción del problema:
        Dado un arreglo o lista 'arr' y un valor 'target', encontrar el índice de la primera
        ocurrencia de 'target' en 'arr'. Si no se encuentra, retornar -1.

    Solución:
        1. Iteramos el arreglo desde la posición 0 hasta len(arr)-1.
        2. En cada iteración, comparamos arr[i] con target.
        3. Si son iguales, retornamos el índice i.
        4. Si terminamos la iteración sin encontrar target, retornamos -1.

    Complejidad:
        - Peor caso (target no está o está al final): recorremos todo el arreglo → O(n) tiempo.
        - Peor espacio: O(1), solo usamos variables auxiliares.
    """
    for i, valor in enumerate(arr):
        if valor == target:
            return i
    return -1


# Ejemplo de uso:
if __name__ == "__main__":
    lista = [5, 3, 8, 2, 9]
    objetivo = 9
    indice = linear_search(lista, objetivo)
    if indice != -1:
        print(f"Elemento {objetivo} encontrado en índice {indice}")
    else:
        print(f"Elemento {objetivo} no encontrado en la lista")
