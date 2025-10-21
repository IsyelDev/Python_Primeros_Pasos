"""
Lucas trabaja en TI y necesita garantizar que la temperatura de una sala de servidores no supere los 25°C. 
Quiere un programa que reciba la temperatura actual como entrada y, si es necesario, muestre un mensaje de alerta.
"""
def mostrarEncabezado():
    print("=" * 35)
    print("=  TEMPERATURA DE LOS SERVIDORES  =")
    print("=" * 35 + "\n")

def temperaturaPermitida(temperatura:int,)->str:
    mensaje = "Alerta: Temperatura por encima del limite permitido." if temperatura > 25 else "Temperatura dentro del rango permitido."
    return mensaje

def obtenerTemperatura()->int:
    temperatura = int(input("Digite la temperatura del servidor: "))
    return temperatura

def main()->None:
    mostrarEncabezado()
    manzana = obtenerTemperatura()
    print(temperaturaPermitida(manzana))

if __name__ == "__main__":
    main()
