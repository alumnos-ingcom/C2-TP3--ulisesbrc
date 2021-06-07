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
    try:
        ingreso = input(mensaje + " #")
        entero = int(ingreso)
        return entero  
    except ValueError as error:
        raise IngresoIncorrecto("No era un entero")

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    """
    Esta funcion llama a la funcion ingreso_entero() y si esta no devuelve un entero
    se llama el numero de veces segun tenga la variable cantidad_reintentos
    """
    while cantidad_reintentos>0:
        try:
            entero = ingreso_entero(mensaje)
            return entero
        except IngresoIncorrecto as err:
            cantidad_reintentos = cantidad_reintentos-1
            print(f"Te quedan {cantidad_reintentos} intentos!")
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
                return entero
            else:
               print(f"Ingresa un número entre {valor_minimo} y {valor_maximo}")
        except IngresoIncorrecto as err:
            print(f"Ingresa un número entre {valor_minimo} y {valor_maximo}")
class IngresoIncorrecto(Exception):
    pass
def prueba():
    ingresar=True
    while ingresar:
        try:
            entero= ingreso_entero("Ingrese un entero")
            ingresar=False
        except IngresoIncorrecto as err:
            print("El valor ingresado no es un entero")
    ingresar=True
    valor_minimo=0
    valor_maximo=10
    while ingresar:
        try:
            entero_restringido_uno= ingreso_entero_restringido(f"Ingrese un entero entre {valor_minimo} y {valor_maximo}",valor_minimo,valor_maximo)
            ingresar=False
        except IngresoIncorrecto as err:
            print("El valor ingresado no es un entero")
    ingresar=True
    cantidad=5
    try:
        entero_reintento= ingreso_entero_reintento(f"Ingrese un entero hasta {cantidad} veces", cantidad)
        ingresar=False
    except IngresoIncorrecto as err:
        raise IngresoIncorrecto("Te quedaste sin intentos!")

if __name__ == "__main__":
    prueba()
   