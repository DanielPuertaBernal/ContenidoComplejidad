def mochila_01(pesos, valores, capacidad):
    """
    Resuelve el problema de la mochila 0/1 usando programación dinámica.

    Parámetros:
        pesos (list[int]): Lista de pesos de los objetos.
        valores (list[int]): Lista de valores de los objetos.
        capacidad (int): Capacidad máxima de la mochila.

    Retorna:
        int: El valor máximo que se puede obtener sin exceder la capacidad.
    """
    n = len(pesos)  # Número de objetos

    # Creamos una matriz (n+1) x (capacidad+1) para almacenar soluciones parciales
    dp = [[0] * (capacidad + 1) for _ in range(n + 1)]

    # Llenamos la tabla dp de abajo hacia arriba
    for i in range(1, n + 1):
        for w in range(1, capacidad + 1):
            if pesos[i - 1] <= w:
                # Caso 1: tomamos el objeto i-1
                valor_tomado = valores[i - 1] + dp[i - 1][w - pesos[i - 1]]
                # Caso 2: no tomamos el objeto i-1
                valor_no_tomado = dp[i - 1][w]
                # Guardamos el máximo de ambos
                dp[i][w] = max(valor_tomado, valor_no_tomado)
            else:
                # No podemos tomar el objeto porque excede el peso disponible
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidad]  # Valor máximo que se puede obtener


# ================================
# Ejemplo de uso:

pesos = [2, 3, 4, 5]       # Pesos de los objetos
valores = [3, 4, 5, 6]     # Valores correspondientes
capacidad = 5              # Capacidad máxima de la mochila

resultado = mochila_01(pesos, valores, capacidad)

print("Valor máximo que se puede obtener:", resultado)