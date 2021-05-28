################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 1. Ingreso de números enteros
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero
def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta funcion llama a la funcion ingreso_entero() y si esta no devuelve un entero
    se llama el numero de veces segun tenga la variable cantidad_reintentos
    """
    while cantidad_reintentos>0:
        try:
            entero = ingreso_entero(mensaje)
            return entero;
        except ValueError as err:
            cantidad_reintentos = cantidad_reintentos-1
            print(f"Te quedan {cantidad_reintentos} intentos!")
            continue
    raise IngresoIncorrecto("Te quedaste sin intentos!")
    
def ingreso_entero_restringido(mensaje, valor_minimo=0, valor_maximo=10):
    """
    Esta funcion llama a la funcion ingreso_entero() limitando ese entero a un
    valor mínimo y un valor máximo segun las variables valor_minimo y valor_máximo
    respectivamente
    """
    solicitar = 1
    while solicitar:
        try:
            entero = ingreso_entero(mensaje)
            if(entero>=valor_minimo and entero<=valor_maximo):
                return entero;
            else:
               print(f"Ingresa un número entre {valor_minimo} y {valor_maximo}")
        except ValueError as err:
            raise IngresoIncorrecto(f"Ingresa un número entre {valor_minimo} y {valor_maximo}") from err
            
class IngresoIncorrecto(Exception):
    pass 


if __name__ == "__main__":
    ingreso_entero("Ingrese un entero")
    ingreso_entero_restringido("Ingrese un entero entre 0 y 10",0,10)    
    ingreso_entero_reintento("Ingrese un entero hasta 5 veces", 5)