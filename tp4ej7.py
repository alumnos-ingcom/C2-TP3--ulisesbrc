################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 7. Restas sucesivas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero_reintento
def division_lenta(dividendo, divisor):
    cociente = 1
    resto = dividendo - divisor
    while resto >= divisor:
        cociente = cociente +1
        resto = resto - divisor
    return (cociente,resto)

def prueba():
    cantidad_de_intentos=10
    dividendo = ingreso_entero_reintento("Ingrese un número entero a ser dividido",cantidad_de_intentos)
    divisor = ingreso_entero_reintento(f"Ingrese un número entero que dividirá a {dividendo}",cantidad_de_intentos)
    divisionlenta = division_lenta(dividendo ,divisor)
    cociente, resto = divisionlenta
    print(f'La division entre {dividendo} y {divisor} da como resultado {cociente} y resto {resto}')
if __name__ == "__main__":
    prueba()