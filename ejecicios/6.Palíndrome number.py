def is_palindrome_number(x: int) -> bool:
    """
    Palindrome Number

    Descripción del problema (LeetCode):
        Dado un entero x, retornar True si x es un palíndromo (es decir, se lee igual hacia adelante
        y hacia atrás). Por ejemplo:
            - x = 121 → True
            - x = -121 → False (por el signo '-')
            - x = 10  → False

    Solución:
            1. Si x < 0: retornar False.
            2. Inicializar backup = x, revertido = 0.
            3. Mientras backup > 0:
                a) dígito = backup % 10
                b) revertido = revertido * 10 + dígito
                c) backup //= 10
            4. Comparar revertido == x.
    """
    if x < 0:
        return False

    # Handle single-digit numbers (including 0)
    if x < 10:
        return True

    # Reverse the number
    reversed_num = 0
    temp_x = x
    while temp_x > 0:
        digit = temp_x % 10
        reversed_num = reversed_num * 10 + digit
        temp_x //= 10

    return x == reversed_num


if __name__ == "__main__":
    test_cases = [121, -121, 10, 12321, 10801, 777]
    for num in test_cases:
        print(f"{num} → {is_palindrome_number(num)}")