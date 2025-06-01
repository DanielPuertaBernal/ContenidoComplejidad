def remove_element(nums, val):
    """
    Remove Element

    Descripción del problema (LeetCode):
        Dado un arreglo 'nums' y un valor 'val', eliminar todas las apariciones de 'val' de nums
        in-place y retornar la nueva longitud del arreglo. El orden de los elementos puede cambiarse.
        No importa lo que haya más allá de la nueva longitud.

    Ejemplo:
        Input: nums = [3,2,2,3], val = 3
        Output: 2, nums modificada = [2,2,_,_]

        Input: nums = [0,1,2,2,3,0,4,2], val = 2
        Output: 5, nums modificada = [0,1,3,0,4,_,_,_]

    Solución:
        - Mantener dos punteros:
            * i = índice que recorre el arreglo.
            * k = conteo de elementos que NO son iguales a val (y al mismo tiempo índice “escribible”).
        - Inicializar k = 0.
        - Para cada i en 0..len(nums)-1:
            • Si nums[i] != val:
                - Asignar nums[k] = nums[i]
                - Incrementar k en 1
            • Si nums[i] == val: ignorar (no incrementamos k).
        - Al final, k será la nueva longitud, y los primeros k elementos de nums serán los que no eran val.
    """
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k


# Ejemplo de uso:
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 0
    print(f"Cadena de los elementos: {nums}")
    new_length = remove_element(nums, val)
    print(f"Longitud después de remover {val}: {new_length}")
    print("Arreglo modificado:", nums[:new_length])