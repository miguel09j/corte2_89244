with open("Alimentos.txt","r") as file:
    dict = {}
    for line in file:
        if len(line.strip().split(",")) >= 3:
            codigo, nombre, tarifa = line.strip().split(",")[-3:]
            dict[codigo] = (nombre,tarifa)

print(dict)

while True:
    busqueda = input("Ingrese el código: ")
    if busqueda.lower() == "salir":
        break
    elif busqueda not in dict:
        print("El código ingresado no se encuentra en la base de datos")
        continue

    p_neto = float(input("Ingrese el valor del producto sin tarifas incluidas: "))
    p_IVA = dict[busqueda][1]
    p_t = p_neto*(1 +float(p_IVA))

    print(f"El precio total con IVA incluido es: {p_t}")

print("Programa terminado")