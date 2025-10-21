
"""
Estás desarrollando un pequeño juego. El usuario ingresa un número entero y el programa debe evaluar lo siguiente:
Si el número es divisible por 3 y 5, muestra: "¡Número mágico!"
Si solo es divisible por 3, muestra: "Divisible por 3"
Si solo es divisible por 5, muestra: "Divisible por 5"
Si no es divisible por ninguno, muestra: "No es un número mágico"
Este tipo de lógica es muy útil en juegos, validaciones o filtros.
"""

def mostrar_encabezado() -> None:
    print("=" * 35)
    print("=         JUEGO MÁGICO NUMÉRICO        =")
    print("=" * 35 + "\n")

def calcular_numero_entero(numero: int) -> str:
    if numero % 15 == 0:  
        return "¡Número mágico!"
    elif numero % 3 == 0:
        return "Divisible por 3"
    elif numero % 5 == 0:
        return "Divisible por 5"
    return "No es un número mágico"

def obtener_numero_entero() -> int:
    while True:
        try:
            numero = int(input("Digite un número entero positivo: "))
            if numero < 0:
                print("El número debe ser positivo. Intente de nuevo.\n")
                continue
            return numero
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero.\n")

def main() -> None:
    mostrar_encabezado()
    numero = obtener_numero_entero()
    resultado = calcular_numero_entero(numero)
    print(f"El resultado es: {resultado}")

if __name__ == "__main__":
    main()