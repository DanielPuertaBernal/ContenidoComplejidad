"""
    Problem A: An Easy-Peasy Problem

    Descripción del problema:
        Travis desea saber si el problema asignado en la competencia de programación es facil o no, para esto:
            - La mitad de los participandes deben resolver correctamente el problema en la mitad del tiempo de la competencia.
            Se pide, a partir de cierta información, calcular y determinar la dificultad del problema de programación asignado.

        Para este ejemplo, definimos:
            - Se ingresa la cantidad de respuestas correctas hasta el momento de la mitad de la competencia.
            - Se ingresa el cantidad toral de respuestas en la competencia
            - Queremos verificar que no se ingresan valores fuera de los posibles en la competencia:
                a) 0 ≤ parte1 ≤ 100 y 0 ≤parte 2 ≤ 100
            - Si no se cumplen, indicar un mensaje de inconsistencia.

    Solución:
        1. Verificamos que las entradas sean números enteros positivos.
        2. Chequeamos la relación entre las respuestas de los participantes.
        4. Si todo es consistente, devolvemos el resultado, si el ejercicio es dificil o no.
    """

def saberDificultad(parte1, parte2):
    if parte1 == 0:
        print("Error: parte1 no puede ser 0")
        return
    if parte2 == 0:
        print("Error: parte2 no puede ser 0")
        return
    
    if parte1 >= parte2 / 2:
        print("E")
    else:
        print("H")

parte1, parte2 = map(int, input().split())

if __name__ == "__main__":
    saberDificultad(parte1, parte2)