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
    minimo = 0
    primero =True
    for i in lista:
        if primero:
            minimo = i
            primero=False
        else:
            if i <minimo:
                minimo=i
    return minimo
def maximo(lista):
    """
    Esta función recibe una lista y devuelve su valor máximo.
    """
    maximo = 0
    primero =True
    for i in lista:
        if primero:
            maximo = i
            primero=False
        else:
            if i >maximo:
                maximo=i
    return maximo
def prueba():
    lista =[55,2,88,645,4,3,7]
    lista_minimo = minimo(lista)
    lista_maximo = maximo(lista)
    print(f'La lista contiene los siguientes valores {lista}')
    print(f'El valor minimo de la lista es {lista_minimo}')
    print(f'El valor maximo de la lista es {lista_maximo}')
if __name__ == "__main__":
    prueba() 