"""
Una escuela otorga becas según tres criterios:

Ingreso familiar mensual.
Promedio del estudiante.
Asistencia (en porcentaje).
Reglas:

Si el ingreso es menor a $1,500 y el promedio es mayor a 8.0 y la asistencia es al menos 90% → "Beca completa"
Si el ingreso es menor a $2,500 y promedio mayor a 7.0 y asistencia al menos 85% → "Media beca"
En otros casos → "No elegible para beca"
"""

def mostrarEncabezado():
    print("=" * 35)
    print("=  BECAS ESCOLARES  =")
    print("=" * 35 + "\n")

def evaluarBecas(ingreso:float, promedio:float, asistencia:float)->str:
    mensaje = ""
    if ingreso < 1500 and promedio > 8.0 and asistencia >= 90:
        mensaje = "Beca completa"
    elif ingreso < 2500 and promedio > 7.0 and asistencia >= 85:
        mensaje = "Media beca"
    else:
        mensaje = "No elegible para beca"
    return mensaje

def ingresarInformacion() -> list:
    informacion = ["ingreso familiar mensual", "promedio", "asistencia"]
    data = [float(input(f"Digite información de {informacion[i]}: ")) for i in range(3)]

    while not all([0 <= data[1] <= 10, 0 <= data[2] <= 100]):
        print("Error: Promedio debe estar entre 0 y 10, y asistencia entre 0 y 100.")
        data = [float(input(f"Digite información de {informacion[i]}: ")) for i in range(3)]

    return data


def main()->None:
    mostrarEncabezado()
    ingreso , promedio , asistencia = ingresarInformacion()
    print(f"El estudiante tiene derecho a {evaluarBecas(ingreso, promedio, asistencia)}")

if __name__ == "__main__":
    main()
