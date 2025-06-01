def dijkstra_matriz(grafo, origen):
    """
    Implementación del algoritmo de Dijkstra usando una matriz de adyacencia.

    Parámetros:
        grafo (list[list[int]]): Matriz de adyacencia donde grafo[i][j] es el peso de la arista i→j.
        origen (int): Índice del nodo desde el cual calcular distancias.

    Retorna:
        distancia (list[float]): Distancia mínima desde el nodo origen a cada nodo.
        predecesor (list[int|None]): Nodo anterior en el camino mínimo hacia cada nodo.
    """

    n = len(grafo)  # Número de nodos en el grafo

    # Inicializamos las distancias a infinito, excepto el nodo de origen (distancia 0)
    distancia = [float('inf')] * n
    distancia[origen] = 0

    # Lista para registrar el nodo anterior en el camino más corto hacia cada nodo
    predecesor = [None] * n

    # Lista para marcar los nodos que ya fueron visitados
    visitado = [False] * n

    # Iteramos hasta visitar todos los nodos
    for _ in range(n):
        # Seleccionamos el nodo no visitado con menor distancia
        u = None
        min_dist = float('inf')
        for i in range(n):
            if not visitado[i] and distancia[i] < min_dist:
                min_dist = distancia[i]
                u = i

        # Si no hay nodo alcanzable, terminamos (restantes son inaccesibles)
        if u is None:
            break

        # Marcamos el nodo como visitado
        visitado[u] = True

        # Recorremos los vecinos del nodo actual
        for v in range(n):
            if not visitado[v]:
                # Calculamos distancia tentativa pasando por u
                nueva_distancia = distancia[u] + grafo[u][v]

                # Si es menor a la actual, actualizamos distancia y predecesor
                if nueva_distancia < distancia[v]:
                    distancia[v] = nueva_distancia
                    predecesor[v] = u

    return distancia, predecesor


# ================================
# Grafo representado como matriz de adyacencia
# Cada posición grafo[i][j] es el peso entre el nodo i y el nodo j
grafo = [
    [ 0, 34, 56, 12, 78, 90, 43, 67, 23, 55 ],
    [ 34, 0, 64, 21, 12, 44, 90, 13, 45, 66 ],
    [ 56, 64, 0, 50, 34, 33, 76, 82, 28, 59 ],
    [ 12, 21, 50, 0, 22, 88, 16, 44, 73, 10 ],
    [ 78, 12, 34, 22, 0, 25, 90, 17, 65, 33 ],
    [ 90, 44, 33, 88, 25, 0, 14, 56, 32, 71 ],
    [ 43, 90, 76, 16, 90, 14, 0, 36, 48, 11 ],
    [ 67, 13, 82, 44, 17, 56, 36, 0, 20, 24 ],
    [ 23, 45, 28, 73, 65, 32, 48, 20, 0, 60 ],
    [ 55, 66, 59, 10, 33, 71, 11, 24, 60, 0 ]
]

# Nodo de partida (origen) para el cálculo de distancias
origen = 0

# Ejecutamos el algoritmo
distancias, predecesores = dijkstra_matriz(grafo, origen)

# Mostrar resultados
print("Distancias desde nodo", origen, ":", distancias)
print("Predecesores:", predecesores)