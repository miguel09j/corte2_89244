def horaio_clases():
    clases = ["fisica","calculo","programacion","investigación","dibujo"]

    profes = ["Bohorquez Avila Roberto","Acuña Gomez Edwin Julian","Torres Barrera David Nicolas","Cortes Roa Julian David","Cepeda Gomez Elmer"]

    horario = ["Martes y Jueves de 9:00 AM- 11:00 AM","Martes y Jueves de 7:00 AM- 9:00 AM","Mrtes y Jueves de 1:00 PM - 3:00 PM "," Viernes de 11:00 AM - 1:00 PM","Viernes de 11:00 AM - 1:00 PM"]

    salon = ["404 DB","407 DB","303 GO","305 DB","305 DB"]

    print(" selecione la materia la cual desea escojer: ")
    print("1. fisica")
    print("2. calcualo")
    print("3, progrmacion")
    print("4. investigacion")
    print("5. dibujo")

    n  = int(input("de que clase quiere saber la informacion: "))

    if n == 1 or 2 or 3 or 4:
        print("la materia la cual selecciono es: ",clases[n-1])
        print("tutor de la clase: ", profes[n-1])
        print("horario de la clase: ", horario[n-1])
        print("salon de la clase: ", salon[n-1])
    else:
        print("revise de nuevo las obciones y escoja una obcion correcta ")

if __name__ == "__main__":
    horaio_clases()