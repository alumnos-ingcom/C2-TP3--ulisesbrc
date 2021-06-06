################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 9. Números primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero
def es_primo(numero):
    if numero<=1:
        return False
    for n in range(2,numero):
        if numero%n==0:
            return False
    return True
def prueba():
    numero = False
    mensaje="Ingrese un número"
    mensaje_error = "Ingrese un número válido"
    while not numero:
        try:
            numero = ingreso_entero(mensaje)
        except:
            print(mensaje_error)
    esprimo = es_primo(numero)
    if esprimo:
        print(f"El número {numero} es primo")
    else:
        print(f"El número {numero} no es primo")
if __name__ == "__main__":
    prueba()