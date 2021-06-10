################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 2. Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero_reintento 

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
    buscar_numero=True
    mensaje="Ingrese un número"
    mensaje_otro="Ingrese otro número"
    mensaje_error="No es un número válido, intente de nuevo"
    cantidad_de_intentos=10
    numero=ingreso_entero_reintento(mensaje,cantidad_de_intentos)
    otro_numero=ingreso_entero_reintento(mensaje_otro,cantidad_de_intentos)
    suma = suma_lenta(numero,otro_numero)
    print(f"La suma lenta entre {numero} y {otro_numero} es {suma}")
if __name__ == "__main__":  
    prueba()