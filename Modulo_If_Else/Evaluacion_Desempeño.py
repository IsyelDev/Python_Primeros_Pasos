"""
Una empresa evalúa a sus empleados con base en dos criterios:

Puntuación de desempeño (de 0 a 10)
Años trabajados
Reglas:

Si la puntuación es mayor o igual a 7:
Si trabajó más de 5 años: "Elegible para ascenso"
Si trabajó 5 años o menos: "Buen desempeño, sigue así"
Si la puntuación es menor a 7: "Necesita mejorar"
Crea un programa que reciba la puntuación y los años trabajados, y muestre el mensaje adecuado.
"""

def mostrarEncabezado():
    print("=" * 35)
    print("=  EVALUACION DE DESEMPEÑO  =")
    print("=" * 35 + "\n")

def evaluarDesempeno(puntuacion:int, años:int)->str:
    mensaje = ""
    if puntuacion >= 7:
        mensaje = "Elegible para ascenso" if años > 5 else "Buen desempeño, sigue así"
    else:
        mensaje = "Necesita mejorar"
    return mensaje

def obtenerInformacion() -> list:
    informacion = ["puntuación", "años trabajados"]

    while True:
        data = [int(input(f"Digite información de {informacion[i]}: ")) for i in range(2)]
        if not all([0 <= data[0] <= 10, data[1] >= 0]):
            print("Entrada inválida. La puntuación debe estar entre 0 y 10, y los años trabajados deben ser 0 o más.\n")
            continue  # vuelve a pedir los datos
        break 
    return data


def main()->None:
    mostrarEncabezado()
    puntuacion , años = obtenerInformacion()
    print(evaluarDesempeno(int(puntuacion), int(años)))

if __name__ == "__main__":
    main()
