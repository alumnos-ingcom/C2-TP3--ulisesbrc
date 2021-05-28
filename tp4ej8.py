################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 8. Ordenar 3 valores
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def ordenar_mayor_a_menor(uno, dos, tres):
    """
    Esta función recibe tres numeros y devuelve esos tres numero ordenados de mayor a menor en una tupla.
    """
    lista = [uno, dos, tres]
    lista.sort(reverse=True)
    uno=lista[0]
    dos=lista[1]
    tres=lista[2]
    tupla = (uno,dos,tres)
    return tupla
def ordenar_menor_a_mayor(uno, dos, tres):
    """
    Esta función recibe tres numeros y devuelve esos tres numero ordenados de menor a mayor en una tupla.
    """
    lista = [uno, dos, tres]
    lista.sort()
    uno=lista[0]
    dos=lista[1]
    tres=lista[2]
    tupla = (uno,dos,tres)
    return tupla

if __name__ == "__main__":
    tupla_ordenada_mayor_a_menor = ordenar_mayor_a_menor(4,3,5)
    tupla_ordenada_menor_a_mayor = ordenar_menor_a_mayor(4,3,5)
    print(f'Los numero numero ingresados son 4,3,5 y la tupla ordenada de mayor a menor es {tupla_ordenada_mayor_a_menor}')
    print(f'Los numero numero ingresados son 4,3,5 y la tupla ordenada de menor a mayor es {tupla_ordenada_menor_a_mayor}')