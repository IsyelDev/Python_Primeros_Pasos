
"""
Un sistema de transporte cobra según la edad del pasajero y la distancia recorrida:

Menores de 6 años: Viajan gratis.
De 6 a 18 años:
Hasta 20 km: $1.50
Más de 20 km: $2.50
Mayores de 18:
Hasta 20 km: $2.50
Más de 20 km: $4.00
Crea un programa que reciba la edad y distancia, y muestre el valor a pagar.
"""

def mostrarEncabezado():
    print("=" * 35)
    print("=  TRANSPORTE EDAD  =")
    print("=" * 35 + "\n")

def calcularCosto(edad: int, distancia: float) -> float:
    if edad < 6:
        return 0.0
    elif edad <= 18:
        return 1.50 if distancia <= 20 else 2.50
    else:
        return 2.50 if distancia <= 20 else 4.00

def obtenerInfo()->tuple:
    informacion = ["edad del pasajero", "distancia recorrida"]
    data =[int(input(f"Digite la {informacion[i]}: ")) for i in range(2)]
    return data

def main()->None:
    mostrarEncabezado()
    edad, distancia = obtenerInfo()
    print(f"El costo a pagar es: ${calcularCosto(edad, distancia):.2f}")

if __name__ == "__main__":
    main()
