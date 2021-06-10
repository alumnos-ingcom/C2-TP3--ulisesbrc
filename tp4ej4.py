################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 4. Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero_reintento
# Reemplazar por las funciones del ejercicio
def compara(numero, otro_numero):
    """
    Esta funcion compara dos numero y devuelve
    -1 si el primero es menor que el segundo
    0 si son iguales
    1 si el primero es mayor que el segundo
    """
    if(numero>otro_numero):
        return 1
    else:
        if(numero<otro_numero):
            return -1
        else:
            return 0
def prueba():
    cantidad_de_intentos=10
    numero=ingreso_entero_reintento("Ingresa un número",cantidad_de_intentos)
    otro_numero=ingreso_entero_reintento("Ingresa otro número",cantidad_de_intentos)
    salida = compara(numero,otro_numero)
    if (salida == 1):
        print(f"el numero {numero} es mayor a {otro_numero}")
    else:
        if (salida == -1):
            print(f"el numero {numero} es menor a {otro_numero}")
        else:
            print(f"el numero {numero} es igual a {otro_numero}")    
    
if __name__ == "__main__":
    prueba()  