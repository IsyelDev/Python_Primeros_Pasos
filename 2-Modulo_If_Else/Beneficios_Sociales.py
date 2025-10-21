"""
Laura está desarrollando un sistema para saber si una persona tiene derecho a recibir un beneficio social. Para eso, la persona debe cumplir las siguientes condiciones:

Tener ingresos menores o iguales a $2,000.
Tener al menos un hijo o hija.
Crea un programa que reciba los ingresos mensuales y la cantidad de hijos de una persona, y diga si tiene derecho al beneficio.
"""
informacion =["ingresos","hijos"]

def mostrarEncabezado():
    print("=" * 35)
    print("=  BENEFICIOS SOCIALES  =")
    print("=" * 35 + "\n")

def tieneDerechoBeneficio(ingresos:float, hijos:int)->bool:
    derecho = ingresos <= 2000 and hijos >= 1
    mensaje = "Tiene derecho al beneficio." if derecho else "No tiene derecho al beneficio."
    return mensaje

def obtenerInformacion()->list:
    data =[input(f"Digite informacion de {informacion[i]}: ") for i in range(2)]
    return data

def main()->None:
    mostrarEncabezado()
    sueldo , hijo = obtenerInformacion()
    print(tieneDerechoBeneficio(float(sueldo), int(hijo)))

if __name__ == "__main__":
    main()
