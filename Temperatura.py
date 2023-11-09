#Autor:Jhoadel Saavedra y Lucas Aldana
#Fecha:06/11/2023
#Descripcion: Este modulo convierte los celsius a fahrenheit

def celsius_fahrenheit(grados):
    return (grados * 9/5) + 32

if __name__=="__main__":

    celsius= float(input("Ingrese los grados a convertir \n"))
    print(celsius_fahrenheit(celsius))