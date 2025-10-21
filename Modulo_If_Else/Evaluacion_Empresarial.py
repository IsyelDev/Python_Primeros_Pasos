
"""
Una empresa evalúa su trimestre con base en:

Ingresos totales
Gastos totales
Número de nuevos clientes
Clasificación:

Si ingresos - gastos > $10,000 y más de 50 nuevos clientes → "Trimestre Excelente"
Si ingresos - gastos > $5,000 y al menos 20 clientes → "Trimestre Bueno"
Si ingresos - gastos > 0 → "Trimestre Regular"
Si ingresos - gastos ≤ 0 → "Trimestre Deficitario"
"""

def mostrarEncabezado():
    print("=" * 35)
    print("=  EVALUACIÓN EMPRESARIAL  =")
    print("=" * 35 + "\n")

def calcularCosto(ingresos: float, gastos: float, nuevosClientes: int) -> str:
    if ingresos - gastos > 10000 and nuevosClientes > 50:
        return "Trimestre Excelente"
    elif ingresos - gastos > 5000 and nuevosClientes >= 20:
        return "Trimestre Bueno"
    elif ingresos - gastos > 0:
        return "Trimestre Regular"
    else:
        return "Trimestre Deficitario"

def obtenerInfo()->tuple:
    informacion = ["ingresos totales", "gastos totales", "nuevos clientes"]
    data =[float(input(f"Digite la {informacion[i]}: ")) for i in range(3)]
    return data

def main()->None:
    mostrarEncabezado()
    ingresos, gastos, nuevosClientes = obtenerInfo()
    print(f"La evaluacion de su desempeño en el trimestre es: ${calcularCosto(ingresos, gastos, nuevosClientes)}")

if __name__ == "__main__":
    main()
