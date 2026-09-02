def calcular_promedio(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    for nota in calificaciones:
        if nota < 0.0 or nota > 5.0:
            raise ValueError("Calificación fuera de rango")

    return sum(calificaciones) / len(calificaciones)
def determinar_estado(calificaciones):
    promedio = calcular_promedio(calificaciones)

    if promedio >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"
def obtener_nota_mayor(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    return max(calificaciones)


def obtener_nota_menor(calificaciones):
    if len(calificaciones) == 0:
        raise ValueError("La lista no puede estar vacía")

    return min(calificaciones)
    
def generar_resumen(calificaciones):
    return {
        "promedio": calcular_promedio(calificaciones),
        "nota_mayor": obtener_nota_mayor(calificaciones),
        "nota_menor": obtener_nota_menor(calificaciones),
        "estado": determinar_estado(calificaciones)
    }


def crear_estudiante(nombre, calificaciones):
    if nombre is None or not nombre.strip():
        raise ValueError("El nombre no puede estar vacío")

    resumen = generar_resumen(calificaciones)

    return {
        "nombre": nombre.strip(),
        "calificaciones": calificaciones,
        **resumen
    }


def generar_resumen_estudiante(estudiante):
    nombre = estudiante["nombre"]
    calificaciones = estudiante["calificaciones"]

    resumen = generar_resumen(calificaciones)

    return {
        "nombre": nombre,
        **resumen
    }