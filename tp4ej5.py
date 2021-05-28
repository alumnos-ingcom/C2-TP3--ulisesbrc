################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 5. Números positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def signo(numero):
    """
    Esta función recibe un número e indica si el mismo es positivo, negativo o cero.
    """
    if(numero>0):
        return "Número positivo"
    else:
        if(numero<0):
            return "Número negativo"
        else:
            return "Número cero"

if __name__ == "__main__":
    numero = signo(4);
    print(f'el 4 es {numero}')
    numero = signo(-4);
    print(f'el -4 es {numero}')
    numero = signo(0);
    print(f'el 0 es {numero}')