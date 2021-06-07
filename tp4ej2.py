################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 2. Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

# Reemplazar por las funciones del ejercicio
def suma_lenta(numero, otro_numero):
    """
    Esta funcion hace la suma lenta entre dos números.
    """
    if(numero>=0):
        while(numero!=0):
            numero=numero-1
            otro_numero=otro_numero+1
        return otro_numero
    else:
        while(numero!=0):
            numero=numero+1
            otro_numero=otro_numero-1
        return otro_numero
def prueba():
    numero=False
    otro_numero=False
    mensaje="Ingrese un número"
    mensaje_otro="Ingrese otro número"
    mensaje_error="No es un número válido, intente de nuevo"
    while not numero:
        try:
            numero=ingreso_entero(mensaje)
        except:
            print(mensaje_error)
    while not otro_numero:
        try:
            otro_numero=ingreso_entero(mensaje_otro)
        except:
            print(mensaje_error)    
    suma = suma_lenta(numero,otro_numero)
    print(f"La suma lenta entre {numero} y {otro_numero} es {suma}")
if __name__ == "__main__":  
    prueba()