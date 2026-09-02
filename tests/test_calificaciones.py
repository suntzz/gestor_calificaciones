from src.calificaciones import calcular_promedio, determinar_estado, obtener_nota_mayor, obtener_nota_menor, generar_resumen, crear_estudiante, generar_resumen_estudiante, buscar_estudiante, obtener_mejor_estudiante, generar_reporte_grupo
import pytest


def test_calcular_promedio_de_tres_notas():
    resultado = calcular_promedio([4.0,3.0, 5.0])
    assert resultado == 4.0


def test_calcular_promedio_lista_vacia():
    with pytest.raises(ValueError):
        calcular_promedio([])


def test_calificaciones_no_pueden_ser_menores_a_cero():
    with pytest.raises(ValueError):
        calcular_promedio([-1.0, 3.0])


def test_calificaciones_no_pueden_ser_mayores_a_cinco():
    with pytest.raises(ValueError):
        calcular_promedio([4.0, 5.5])


def test_valores_limite_son_validos():
    resultado = calcular_promedio([0.0, 5.0])
    assert resultado == 2.5


def test_determinar_estado_aprobado():
    resultado = determinar_estado([3.0, 3.0, 3.0])
    assert resultado == "Aprobado"


def test_determinar_estado_reprobado():
    resultado = determinar_estado([2.0, 3.0, 2.0])
    assert resultado == "Reprobado"


def test_obtener_nota_mayor():
    resultado = obtener_nota_mayor([4.0, 3.0, 5.0, 3.5])
    assert resultado == 5.0


def test_obtener_nota_menor():
    resultado = obtener_nota_menor([4.0, 3.0, 5.0, 3.5])
    assert resultado == 3.0


def test_obtener_nota_mayor_lista_vacia():
    with pytest.raises(ValueError):
        obtener_nota_mayor([])


def test_obtener_nota_menor_lista_vacia():
    with pytest.raises(ValueError):
        obtener_nota_menor([])


def test_generar_resumen():
    resultado = generar_resumen([4.0, 3.0, 5.0])

    assert resultado == {
        "promedio": 4.0,
        "nota_mayor": 5.0,
        "nota_menor": 3.0,
        "estado": "Aprobado"
    }


def test_crear_estudiante_con_datos_validos():
    resultado = crear_estudiante("Ana", [4.0, 3.0, 5.0])

    assert resultado == {
        "nombre": "Ana",
        "calificaciones": [4.0, 3.0, 5.0],
        "promedio": 4.0,
        "nota_mayor": 5.0,
        "nota_menor": 3.0,
        "estado": "Aprobado"
    }


def test_crear_estudiante_nombre_vacio():
    with pytest.raises(ValueError):
        crear_estudiante("   ", [4.0, 3.0, 5.0])


def test_crear_estudiante_calificaciones_invalidas():
    with pytest.raises(ValueError):
        crear_estudiante("Ana", [])


def test_generar_resumen_estudiante_aprobado():
    estudiante = {"nombre": "Ana", "calificaciones": [4.0, 3.0, 5.0]}

    resultado = generar_resumen_estudiante(estudiante)

    assert resultado == {
        "nombre": "Ana",
        "promedio": 4.0,
        "nota_mayor": 5.0,
        "nota_menor": 3.0,
        "estado": "Aprobado"
    }


def test_generar_resumen_estudiante_reprobado():
    estudiante = {"nombre": "Luis", "calificaciones": [2.0, 2.5, 2.0]}

    resultado = generar_resumen_estudiante(estudiante)

    assert resultado == {
        "nombre": "Luis",
        "promedio": 2.1666666666666665,
        "nota_mayor": 2.5,
        "nota_menor": 2.0,
        "estado": "Reprobado"
    }


def test_buscar_estudiante_existente():
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [4.0, 3.5]},
        {"nombre": "Carlos", "calificaciones": [2.5, 3.0]},
    ]

    resultado = buscar_estudiante(estudiantes, "Carlos")

    assert resultado == {"nombre": "Carlos", "calificaciones": [2.5, 3.0]}


def test_buscar_estudiante_inexistente():
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [4.0, 3.5]},
        {"nombre": "Carlos", "calificaciones": [2.5, 3.0]},
    ]

    with pytest.raises(ValueError):
        buscar_estudiante(estudiantes, "Pedro")


def test_obtener_mejor_estudiante_con_mayor_promedio():
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [4.0, 5.0]},
        {"nombre": "Luis", "calificaciones": [3.0, 3.0]},
        {"nombre": "Carlos", "calificaciones": [3.0, 4.0]},
    ]

    resultado = obtener_mejor_estudiante(estudiantes)

    assert resultado == {"nombre": "Ana", "calificaciones": [4.0, 5.0]}


def test_obtener_mejor_estudiante_empate():
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [4.0, 4.0]},
        {"nombre": "Luis", "calificaciones": [3.0, 5.0]},
        {"nombre": "Carlos", "calificaciones": [2.0, 6.0]},
    ]

    with pytest.raises(ValueError):
        obtener_mejor_estudiante(estudiantes)


def test_generar_reporte_grupo():
    estudiantes = [
        {"nombre": "Ana", "calificaciones": [4.0, 5.0]},
        {"nombre": "Luis", "calificaciones": [2.0, 3.0]},
        {"nombre": "Carlos", "calificaciones": [3.0, 4.0]},
    ]

    resultado = generar_reporte_grupo(estudiantes)

    assert resultado == {
        "total_estudiantes": 3,
        "promedio_general": 3.5,
        "aprobados": 2,
        "reprobados": 1,
        "mejor_estudiante": "Ana"
    }


def test_generar_reporte_grupo_lista_vacia():
    with pytest.raises(ValueError):
        generar_reporte_grupo([])