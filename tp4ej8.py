################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 8. Ordenar 3 valores
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero
def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función recibe tres numeros y devuelve esos tres numero ordenados de mayor a menor en una tupla.
    """
    a=uno
    b=dos
    c=tres
    if (a>=b):
        if a>=c:
            if c>=b:
                return a,c,b
            else:
                return a,b,c
        else:
            return c,a,b
    else:
        if b>=c:
            if c>=a:
                return b,c,a
            else:
                return b,a,c
        else:
            return c,b,a
    if(a>=c):
        if a>=b:
            if b>=c:
                return a,b,c
            else:
                return a,c,b
        else:
            return b,a,c
    else:
        if c>=b:
            if b>=a:
                return c,b,a
            else:
                return c,a,b
        else:
            return b,c,a

def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función recibe tres numeros y devuelve esos tres numero ordenados de menor a mayor en una tupla.
    """
    a=uno
    b=dos
    c=tres
    if (a>=b):
        if a>=c:
            if c>=b:
                return b,c,a #cambio el orden de la funcion anterior
            else:
                return c,b,a
        else:
            return b,a,c
    else:
        if b>=c:
            if c>=a:
                return a,c,b
            else:
                return c,a,b
        else:
            return a,b,c
    if(a>=c):
        if a>=b:
            if b>=c:
                return c,b,a
            else:
                return b,c,a
        else:
            return c,a,b
    else:
        if c>=b:
            if b>=a:
                return a,b,c
            else:
                return b,a,c
        else:
            return b,c,a
def prueba():
    mensaje_error = "Ingrese un número válido"
    mensaje="Ingrese un número"
    uno = False
    dos = False
    tres = False
    while not uno:
        try:
            uno = ingreso_entero(mensaje)
        except:
            print(mensaje_error)
    while not dos:
        try:
            dos = ingreso_entero(mensaje)
        except:
            print(mensaje_error)
    while not tres:
        try:
            tres = ingreso_entero(mensaje)
        except:
            print(mensaje_error)
    tupla_ordenada_mayor_a_menor = ordenar_mayor_a_menor(uno,dos,tres)
    tupla_ordenada_menor_a_mayor = ordenar_menor_a_mayor(uno,dos,tres)
    print(f'Los numeros ingresados son {uno},{dos},{tres} y la tupla ordenada de mayor a menor es {tupla_ordenada_mayor_a_menor}')
    print(f'Los numeros ingresados son {uno},{dos},{tres} y la tupla ordenada de menor a mayor es {tupla_ordenada_menor_a_mayor}')
if __name__ == "__main__":
    prueba()