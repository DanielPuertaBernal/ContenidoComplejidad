def cambio_voraz(monto, denominaciones):
    """
    Algoritmo voraz para devolver cambio utilizando la menor cantidad de monedas/billetes posibles.

    Parámetros:
        monto (int): Cantidad de dinero a devolver.
        denominaciones (list[int]): Lista de monedas o billetes disponibles (en orden cualquiera).

    Retorna:
        dict[int, int]: Diccionario donde clave = denominación, valor = cantidad usada.
    """
    # Ordenar denominaciones de mayor a menor (estrategia voraz)
    denominaciones.sort(reverse=True)

    resultado = {}  # Para almacenar cuántas monedas/billetes usamos

    for d in denominaciones:
        if monto >= d:
            cantidad = monto // d  # Cuántas veces cabe la denominación
            resultado[d] = cantidad
            monto -= cantidad * d  # Reducimos el monto restante

    # Si monto no se pudo cubrir exactamente, mostrar advertencia
    if monto > 0:
        print("No se pudo devolver el monto exacto con las denominaciones dadas.")

    return resultado

denominaciones = [50, 20, 10, 5, 2, 1]
monto = 147

cambio = cambio_voraz(monto, denominaciones)

print("Cambio devuelto:")
for denom, cantidad in cambio.items():
    print(f"{cantidad} x {denom}")