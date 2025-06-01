def superDigit(n, k):
    """
    Calcula el superdígito de un número grande formado al repetir 'n' 'k' veces.

    Parámetros:
        n (str): Número base como cadena.
        k (str/int): Cuántas veces repetir el número base.

    Retorna:
        int: El superdígito del número construido.
    """


    def digit_sum(num: str) -> int:
        """
        Función recursiva que calcula el superdígito de un número.

        Si el número tiene un solo dígito, lo retorna.
        Si no, suma sus dígitos y llama a sí misma con el resultado.
        """
        if len(num) == 1:
            return int(num)  # Caso base: un solo dígito, se retorna directamente
        # Suma de los dígitos, luego se llama recursivamente
        return digit_sum(str(sum(int(d) for d in num)))

    # En lugar de construir n*k (lo cual sería enorme), sumamos los dígitos de 'n' y los multiplicamos por k
    initial_sum = sum(int(d) for d in n) * int(k)

    # Calculamos el superdígito de ese valor
    return digit_sum(str(initial_sum))


if __name__ == '__main__':
    # Leer la entrada desde la consola, separando los valores por espacio
    first_multiple_input = input("Ingresa n y k separados por espacio: ").rstrip().split()
    n = first_multiple_input[0]  # Número base como string
    k = first_multiple_input[1]  # Veces a repetir

    # Calcular el resultado y mostrarlo
    result = superDigit(n, k)
    print(result)