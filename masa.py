#Autor:Lucas Aldana, Jhoadel Saavedra
#Fecha:06/11/2023
#Descripcion: Este modulo convierte los kilos a gramos

def Kilos_gramos(kilos):
    return (kilos * 1000)

if __name__=="__main__":

    kilos= float(input("Ingrese los kilos a convertir \n"))
    print(Kilos_gramos(kilos))