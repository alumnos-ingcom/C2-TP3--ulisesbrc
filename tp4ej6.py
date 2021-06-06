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
def prueba():
    lista =[55,2,88,645,4,3,7]
    lista_minimo = minimo(lista)
    lista_maximo = maximo(lista)
    print(f'La lista contiene los siguientes valores {lista}')
    print(f'El valor minimo de la lista es {lista_minimo}')
    print(f'El valor maximo de la lista es {lista_maximo}')
if __name__ == "__main__":
    prueba() 