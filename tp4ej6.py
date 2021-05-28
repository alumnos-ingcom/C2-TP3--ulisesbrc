################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 6. Máximo / Mínimo
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def minimo(lista):
    """
    Esta función recibe una lista y devuelve su valor minimo.
    """
    lista.sort()
    return lista[0]
def maximo(lista):
    """
    Esta función recibe una lista y devuelve su valor máximo.
    """
    lista.sort(reverse=True)
    return lista[0]
    pass
if __name__ == "__main__":
    lista =[55,2,88,645,4,3,7]
    minimo = minimo(lista)
    maximo = maximo(lista)
    print(f'La lista contiene los siguientes valores {lista}')
    print(f'El valor minimo de la lista es {minimo}')
    print(f'El valor maximo de la lista es {maximo}')