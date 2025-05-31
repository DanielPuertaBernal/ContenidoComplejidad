def remove_duplicates_sorted_array(nums):
    """
    Remove Duplicates from Sorted Array

    Descripción del problema (LeetCode):
        Dado un arreglo ordenado 'nums', modificarlo in-place para que cada elemento aparezca solo
        una vez y retornar la nueva longitud. No importa lo que haya más allá de la nueva longitud.
        Devuelve la longitud k (k ≤ len(nums)) tal que los primeros k elementos de nums contienen
        los valores únicos en su orden relativo original.

    Ejemplo:
        Input:  nums = [1,1,2]
        Output: k = 2, nums = [1,2,_]

        Input:  nums = [0,0,1,1,1,2,2,3,3,4]
        Output: k = 5, nums = [0,1,2,3,4,_,_,_,_,_]

    Solución:
        - Mantener dos punteros:
            * i = índice para el elemento “escribible” (última posición de elementos únicos encontrados).
            * j = índice que recorre todo el arreglo.
        - Inicializar i = 0 (si el arreglo no está vacío);
          j partirá desde 1 hasta len(nums)-1.
        - Para cada j:
            • Si nums[j] != nums[i]: significa que encontramos un nuevo valor único.
            • Incrementar i en 1. Asignar nums[i] = nums[j].
        - Al final, la cantidad de elementos únicos es i + 1.
    """
    if not nums:
        return 0

    # i es el índice del último elemento único encontrado
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    # Finalmente, la longitud de la sublista única es i+1
    return i + 1


# Ejemplo de uso:
if __name__ == "__main__":
    nums1 = [1, 1, 2]
    k1 = remove_duplicates_sorted_array(nums1)
    print(f"Longitud única: {k1}, Arreglo modificado: {nums1[:k1]}")

    nums2 = [0,0,0,1,1,1,2,2,3,3,4]
    k2 = remove_duplicates_sorted_array(nums2)
    print(f"Longitud única: {k2}, Arreglo modificado: {nums2[:k2]}")
