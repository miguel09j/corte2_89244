import math

def trigonometricas():
    print("seleccione la funcion trigonometrica la cual desea ejecutar: ")
    print("1. funcion seno")
    print("")
    print("2. funcion coseno")
    print("")
    print("3. funcion tangente")
    print("")
    print("4. funcion exponencial")
    print("")
    print("5. funcion de lagaritmo natural")
    n = int(input("ingrese la opcion la cual desea escojer: "))

    if n == 1:
        sin = float(input("ingrese un numero: "))
        sin = math.sin(sin)
        print("el seno es igual a: ",sin)
    elif n == 2:
        cos = float(input("ingrese un numero: "))
        cos = math.cos(cos)
        print("el seno es igual a: ",cos)
    elif n == 3:
        tan = float(input("ingrese un numero: "))
        tan = math.tan(tan)
        print("la tangente es igual a: ",tan)
    elif n == 4:
        exp = float(input("ingrese un numero: "))
        exp = math.exp(tan)
        print("la exponencial es igual a: ",exp)
    elif n == 5:
        lgn = float(input("ingrese un numero:"))
        lgn = math.log(lgn)
        print("el logaritmo es igual a: ",lgn)

if __name__ == "__main__":
    trigonometricas()