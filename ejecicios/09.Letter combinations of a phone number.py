def letter_combinations(digits):
    """
    Letter Combinations of a Phone Number

    Descripción del problema (LeetCode):
        Dado un string 'digits' que contiene dígitos del 2 al 9 inclusive, retornar todas las
        posibles combinaciones de letras que el número podría representar, en el orden arbitrario.
        El mapeo de dígitos a letras es el mismo que en un teclado antiguo:
            2 → "abc"
            3 → "def"
            4 → "ghi"
            5 → "jkl"
            6 → "mno"
            7 → "pqrs"
            8 → "tuv"
            9 → "wxyz"
        Si digits está vacío, debe retornar [].

    Solución:
        1. Usar backtracking (DFS) para construir combinaciones:
            a) Definir un diccionario mapping que asocie cada dígito con sus letras.
            b) Si digits == "", retornar [] inmediatamente.
            c) Definir una lista resultado = [] para almacenar combinaciones finales.
            d) Definir una función recursiva backtrack(index, path):
                - index: posición actual dentro de la cadena digits que estamos procesando.
                - path: string acumulado de letras hasta el momento.
                - Si index == len(digits), significa que hemos construido una combinación completa:
                    • Append path a resultado.
                    Retornar.
                - Obtener el dígito actual: digit = digits[index].
                - Obtener las letras asociadas: letters = mapping[digit].
                - Iterar cada letra en letters:
                    • Llamar recursivamente backtrack(index + 1, path + letra).

    Complejidad:
        - Tiempo: O(4^n * n), donde n = len(digits). En el peor caso, el dígito '7' o '9' tienen 4 letras,
            así que hay 4^n combinaciones, y para cada combinación construimos un string de longitud n.
        - Espacio: O(n) en la pila de recursión más el espacio para almacenar las combinaciones (O(4^n) cadenas).
    """
    if not digits:
        return []

    # Mapeo de dígitos a letras
    mapping = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    resultado = []

    def backtrack(index, path):
        # index: posición actual en digits; path: combinación parcial
        if index == len(digits):
            # Si llegamos al final, agregamos la combinación actual
            resultado.append(path)
            return
        current_digit = digits[index]
        letters = mapping.get(current_digit, "")
        for letter in letters:
            backtrack(index + 1, path + letter)

    # Iniciamos la recursión desde la posición 0 con path vacío
    backtrack(0, "")
    return resultado


# Ejemplo de uso:
if __name__ == "__main__":
    input_digits = "23"
    combos = letter_combinations(input_digits)
    print(f"Combinaciones para '{input_digits}': {combos}")
