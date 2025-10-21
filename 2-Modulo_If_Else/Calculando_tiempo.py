"""
Camila está organizando un proyecto y necesita calcular el tiempo total necesario para concluir tres actividades: A, B y C. Sin embargo, si alguna actividad tiene un número de días negativo, el código debe avisar que los valores ingresados son inválidos y no calcular el total.

Escribe un programa que reciba el número de días de tres actividades y muestre el tiempo total del proyecto. Si algún valor es negativo, muestra un mensaje informando el error.
"""
proyectos =["A","B","C"]

def mostrarEncabezado():
    print("=" * 35)
    print("=  CALCULANDO TIEMPO TOTAL  =")
    print("=" * 35 + "\n")

def ingresardata(proyectos:list,rango=3)->tuple:
    data = [ int(input(f"Informe los dias para la actividad {proyectos[i]}: ")) for i in range(rango)]
    return data

def valoresNoNegativos(data:tuple)->bool:
    if all(dias > 0 for dias in data):
        mensaje = f"Los dias para terminar las actividades {proyectos} seran de: {sum(data)} días"
    else:
        mensaje = "Error: Los valores ingresados no pueden ser negativos."
    print(mensaje)
    return mensaje

def main()->None:
    mostrarEncabezado()
    valoresNoNegativos(ingresardata(proyectos))

if __name__ == "__main__":
    main()

