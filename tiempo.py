#Autor:Lucas Aldana, Jhoadel Saavedra
#Fecha:06/11/2023
#Descripcion: Este Modulo convierte las horas a minutos

def horas_mins(minutos):
    return (minutos*60)

if __name__=="__main__":

    minutos= float(input("Ingrese los minutos a convertir \n"))
    print(horas_mins(minutos))
    