################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 9. Números primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero_reintento
def es_primo(numero):
    if numero<=1:
        return False
    for n in range(2,numero):
        if numero%n==0:
            return False
    return True
def prueba():
    cantidad_de_intentos=10
    mensaje="Ingrese un número"
    numero = ingreso_entero_reintento(mensaje,cantidad_de_intentos)
    esprimo = es_primo(numero)
    if esprimo:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")
if __name__ == "__main__":
    prueba()