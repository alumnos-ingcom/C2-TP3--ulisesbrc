################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 4. Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################
class IngresoIncorrecto(Exception):
    pass
def ingrese_numero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número.
    """
    try:
        numero = float(input(mensaje + " #"))
        return numero  
    except ValueError as error:
        raise IngresoIncorrecto("No era un número")

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
    ingresar = True
    while ingresar:
        try:
            numero=ingrese_numero("Ingresa un número")
            ingresar=False
        except:
            print("El valor ingresado no es correcto")
            ingresar=True
            continue
    ingresar = True
    while ingresar:
        try:
            otro_numero=ingrese_numero("Ingresa otro número")
            ingresar=False
        except:
            print("El valor ingresado no es correcto")
            ingresar=True
            continue
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