################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 2. Suma lenta
# UNRN Andina - Introducción a la Ingenieria en Computación
################


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


if __name__ == "__main__":
    suma = suma_lenta(-4,-44)
    print(suma)