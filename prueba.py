empleados = [
    {"rol": "vigilante", "cantidad": 5, "salario": 300},
    {"rol": "docente", "cantidad": 16, "salario": 500},
    {"rol": "coordinador", "cantidad": 2, "salario": 600}
]

def sumar_cantidad(empleados: list[dict]) -> int:
    """Suma la cantidad total de empleados."""
    total = sum(f["cantidad"] for f in empleados)
    print(f"La cantidad total de empleados es de {total}")
    return total

def diferencia(coordinador: dict, vigilante: dict) -> int:
    """Calcula la diferencia de salario entre el coordinador y el vigilante."""
    diferencia = coordinador["salario"] - vigilante["salario"]
    print(f"La diferencia de salario entre el coordinador y el vigilante es de {diferencia}")
    return diferencia

def promedio_ponderado(empleados: list[dict]) -> float:
    """Calcula el promedio ponderado de los salarios."""
    total_salarios = sum(e["salario"] * e["cantidad"] for e in empleados)
    total_empleados = sum(e["cantidad"] for e in empleados)
    promedio = total_salarios / total_empleados
    print(f"El promedio ponderado de los salarios es de {round(promedio, 2)}")
    return round(promedio, 2)

def main()->None:
    sumar_cantidad(empleados)
    diferencia(empleados[2], empleados[0])
    promedio_ponderado(empleados)

if __name__ == "__main__":
    main()
