# Ciudadano

# __Nombre:str

# __Cedula:int

# __Edad:int

# +Ciudadano()

# +getNombre():str

# +getCedula():int

# +getEdad():int

# +setNombre(nombre: str)

# +setCedula(cedula)

# -EsMayorDeEdad(edad):mayorEdad

# +getEsMayorDeEdad():str









class Ciudadano:

    def __init__(self,nombre:str,cedula:int,edad:int,mayor_de_edad:int):
            self.__Nombre = nombre
            self.__Cedula = cedula
            self.__Edad = edad
            self.__Mayor_De_Edad = mayor_de_edad

# ---------------Getters------------------------------
    
    def getNombre(self):
        return self.__Nombre
    
    def getCedula(self):
        return self.__Cedula
    
    def getEdad(self):
        return self.__Edad
    
    def getMayorEdad(self):
        return self.__Edad >= 18
    
#-----------------Setters-----------------------------
    

    def setNombre(self, nombre:str):
        self.__Nombre = nombre

    def setCedula(self, cedula:int):
        if 8 <= len(str(cedula)) <= 10:
            self.__Cedula = cedula
        else:
            print("Error: La cédula debe tener entre 8 y 10 dígitos.")

    def setedad(self,edad:int):
        if edad > 0:
            self.__Edad = edad
        else: 
            print("Error: la edad debe ser mayor a cero")

    


def main():

    nico = Ciudadano("Nicolas",15672515,20,20)

    print("Ciudadano: ")
    print("")
    print(f"Nombre: {nico.getNombre()}")
    print(f"Cedula: {nico.getCedula()}")
    print(f"Edad: {nico.getEdad()}")
    if nico.getMayorEdad():
        print("El ciudadano es mayor de edad.")
    else:
        print("El ciudadano no es mayor de edad.")




if __name__ == "__main__":
    main()