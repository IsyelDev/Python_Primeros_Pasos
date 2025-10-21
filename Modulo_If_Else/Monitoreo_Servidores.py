"""
Crea un programa que reciba el número de ventas de los dos productos y muestre un mensaje 
indicando cuál de ellos vendió más. Si las cantidades son iguales, muestra un mensaje diciendo que hubo un empate.
"""
def mostrar_encabezado():
    print("=" * 35)
    print("=  MONITOREO DE VENTAS DE FRUTAS  =")
    print("=" * 35 + "\n")


def comparar_ventas(manzana:int, platano:int)->str:
    if manzana > platano:
        mensaje= f"El producto más vendido fue manzanas con una cantidad: {manzana}"
    elif platano > manzana:
        mensaje= f"El producto más vendido fue plátanos con una cantidad: {platano}"
    else:
        mensaje = "Ambos productos son iguales"
    print(mensaje)
    return mensaje

def obtener_ventas()->tuple:
    manzana = int(input("Digite la cantidad de manzanas vendidas: "))
    platano = int(input("Digite la cantidad de plátanos vendidas: "))
    return manzana, platano


def main()->None:
    mostrar_encabezado()
    manzana, platano = obtener_ventas()
    comparar_ventas(manzana, platano)

if __name__ == "__main__":
    main()
