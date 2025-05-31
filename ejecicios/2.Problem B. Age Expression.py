def problem_b_age_expression(current_age_grandpa, age_alyssa, age_konari):
    """
    Problem B: Age Expression (Dr. O y sus 2 nietas Alyssa y Konari)

    Descripción del problema:
        El enunciado típico de este problema indica que:
          - El Dr. O, Alyssa y Konari tienen diferentes edades.
          - Hay una relación (o varias) entre esas edades. Por ejemplo:
                1) Alyssa es la mitad de la edad de Dr. O.
                2) Konari es 3 años menor que Alyssa.
                3) Se sabe la suma total de sus edades.
            Se pide, a partir de cierta información, calcular las edades actuales de Alyssa y Konari 
            o determinar en qué año ocurrió un evento relacionado con sus edades.

        Para este ejemplo, definimos:
          - Se ingresa la edad actual del Dr. O, Alyssa y Konari.
          - Queremos verificar si las relaciones entre edades se cumplen:
                a) Alyssa == Dr. O // 2
                b) Konari == Alyssa - 3
          - Si no se cumplen, indicar un mensaje de inconsistencia.
          - En caso de consistencia, retornar un diccionario con sus edades.

    Solución:
        1. Verificamos que las entradas sean números enteros positivos.
        2. Chequeamos cada relación de edad:
             a) age_alyssa == current_age_grandpa // 2
             b) age_konari == age_alyssa - 3
        3. Si alguna relación no se cumple, retornamos un mensaje de error.
        4. Si todo es consistente, devolvemos un diccionario con las tres edades.
    """
    # Validación de tipos y valores
    for nombre, valor in [("Dr. O", current_age_grandpa), ("Alyssa", age_alyssa), ("Konari", age_konari)]:
        if not isinstance(valor, int) or valor < 0:
            raise ValueError(f"La edad de {nombre} debe ser un entero no negativo.")

    # Relación 1: Alyssa es la mitad de la edad de Dr. O (suponemos división entera)
    if age_alyssa != current_age_grandpa // 2:
        return f"Inconsistencia: Alyssa ({age_alyssa}) no es la mitad de Dr. O ({current_age_grandpa})."

    # Relación 2: Konari es 3 años menor que Alyssa
    if age_konari != age_alyssa - 3:
        return f"Inconsistencia: Konari ({age_konari}) no es 3 años menor que Alyssa ({age_alyssa})."

    # Si llegamos acá, las edades concuerdan
    return {
        "Dr. O": current_age_grandpa,
        "Alyssa": age_alyssa,
        "Konari": age_konari
    }


# Ejemplo de uso:
if __name__ == "__main__":
    # Supongamos que Dr. O tiene 60 años, Alyssa debe tener 30, y Konari 27
    resultado = problem_b_age_expression(60, 30, 27)
    print("Resultado:", resultado)
