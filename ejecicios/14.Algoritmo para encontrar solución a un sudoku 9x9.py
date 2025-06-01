def imprimir_sudoku(tablero):
    """
    Imprime el tablero de Sudoku.
    Los ceros se muestran como puntos (.) para indicar casillas vacías.
    """
    for fila in tablero:
        # Convertimos cada número a string; si es 0, mostramos '.' en su lugar
        print(" ".join(str(num) if num != 0 else '.' for num in fila))


def es_valido(tablero, fila, col, num):
    """
    Verifica si se puede colocar 'num' en la posición (fila, col) sin romper las reglas del Sudoku.

    Reglas del Sudoku:
        - No se puede repetir un número en la misma fila
        - No se puede repetir en la misma columna
        - No se puede repetir en el mismo bloque 3x3
    """
    # Verifica si 'num' ya está en la fila
    if num in tablero[fila]:
        return False

    # Verifica si 'num' ya está en la columna
    for i in range(9):
        if tablero[i][col] == num:
            return False

    # Verifica si 'num' ya está en el bloque 3x3 al que pertenece (fila, col)
    inicio_fila = 3 * (fila // 3)
    inicio_col = 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if tablero[inicio_fila + i][inicio_col + j] == num:
                return False

    # Si pasa todas las pruebas, es válido colocar el número
    return True


def resolver_sudoku(tablero):
    """
    Resuelve el tablero de Sudoku usando backtracking.

    Busca una celda vacía (con 0), intenta colocar un número válido del 1 al 9,
    y llama recursivamente para continuar llenando el tablero.

    Si en algún punto no se puede continuar, retrocede (backtrack).
    """
    for fila in range(9):
        for col in range(9):
            # Buscar la primera casilla vacía
            if tablero[fila][col] == 0:
                # Probar con números del 1 al 9
                for num in range(1, 10):
                    if es_valido(tablero, fila, col, num):
                        # Colocar número tentativamente
                        tablero[fila][col] = num
                        # Llamar recursivamente para continuar
                        if resolver_sudoku(tablero):
                            return True
                        # Si falla, deshacer movimiento (backtrack)
                        tablero[fila][col] = 0
                # Si ningún número es válido en esta celda, no hay solución desde aquí
                return False
    # Si no quedan celdas vacías, el Sudoku está resuelto
    return True


# Tablero de Sudoku con ceros representando celdas vacías
tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Mostrar Sudoku original
print("Sudoku inicial:")
imprimir_sudoku(tablero)

# Resolver Sudoku y mostrar resultado
if resolver_sudoku(tablero):
    print("\nSudoku resuelto:")
    imprimir_sudoku(tablero)
else:
    print("\nNo hay solución para el Sudoku dado.")