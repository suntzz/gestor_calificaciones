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


def buscar_estudiante(estudiantes, nombre):
    for estudiante in estudiantes:
        if estudiante["nombre"] == nombre:
            return estudiante

    raise ValueError(f"Estudiante no encontrado: {nombre}")


def obtener_mejor_estudiante(estudiantes):
    if len(estudiantes) == 0:
        raise ValueError("La lista no puede estar vacía")

    mejor_estudiante = None
    mejor_promedio = None

    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["calificaciones"])

        if mejor_promedio is None or promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante = estudiante
        elif promedio == mejor_promedio:
            raise ValueError("Hay varios estudiantes con el mismo promedio más alto")

    return mejor_estudiante


def generar_reporte_grupo(estudiantes):
    if len(estudiantes) == 0:
        raise ValueError("La lista no puede estar vacía")

    promedios = [calcular_promedio(estudiante["calificaciones"]) for estudiante in estudiantes]
    promedio_general = calcular_promedio(promedios)

    aprobados = 0
    for estudiante in estudiantes:
        if determinar_estado(estudiante["calificaciones"]) == "Aprobado":
            aprobados += 1

    reprobados = len(estudiantes) - aprobados
    mejor_estudiante = obtener_mejor_estudiante(estudiantes)

    return {
        "total_estudiantes": len(estudiantes),
        "promedio_general": promedio_general,
        "aprobados": aprobados,
        "reprobados": reprobados,
        "mejor_estudiante": mejor_estudiante["nombre"]
    }