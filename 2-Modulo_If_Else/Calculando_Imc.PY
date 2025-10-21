"""
Anna Júlia está creando un sistema para calcular el Índice de Masa Corporal (IMC) 
y proporcionar recomendaciones básicas. 
El programa debe recibir el peso y la altura de una persona y mostrar el valor del IMC, 
además de indicar si está por debajo del peso, con peso normal o por encima del peso. 
Crea un programa que reciba el peso (en kg) y la altura (en metros) y 
calcule el IMC usando la fórmula: IMC = peso / (altura ** 2)Luego, 
muestra el valor del IMC y un mensaje indicando si está por debajo del peso
(IMC < 18.5), peso normal (18.5 <= IMC < 25) o por encima del peso (IMC >= 25).
"""
informacion = [{"peso":"(kg)","altura":"(m)"}]
def mostrarEncabezado():
    print("=" * 35)
    print("=           CALCULANDO IMC        =")
    print("=" * 35 + "\n")

def obtenerPesoAltura()->int:
    peso = float(input("Digite su peso " + informacion[0]["peso"] + " "))
    altura = float(input("Digite su altura " + informacion[0]["altura"] + " "))
    return peso,altura

def calcularIMC(peso:float,altura:float)->float:
    imc = peso / (altura ** 2)
    print("Su IMC es " + str(round(imc,2)))
    return imc

def interpretarIMC(imc:float)->str:
    if imc < 18.5:
        mensaje = "Por debajo del peso."
    elif imc < 25:
        mensaje = "Tienes Peso normal."
    else:
        mensaje = "Por encima del peso."
    return mensaje

def main()->None:
    mostrarEncabezado()
    peso,altura = obtenerPesoAltura()
    imc = calcularIMC(peso,altura)
    print(interpretarIMC(imc))

if __name__ == "__main__":
    main()
