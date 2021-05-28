################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 4. Comparación de números
# UNRN Andina - Introducción a la Ingenieria en Computación
################


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

if __name__ == "__main__":
    salida = compara(9,6);
    print(f'9 > 6 salida {salida}')
    salida = compara(6,9);
    print(f'6 < 9 salida {salida}')
    salida = compara(9,9);
    print(f'9=9 salida {salida}')