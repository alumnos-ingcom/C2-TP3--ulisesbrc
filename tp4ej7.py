################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 7. Restas sucesivas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero
def division_lenta(dividendo, divisor):
    cociente = 1
    resto = dividendo - divisor
    while resto >= divisor:
        cociente = cociente +1
        resto = resto - divisor
    return (cociente,resto)

def prueba():
    dividendo = False
    divisor = False
    mensaje_error = "Ingrese un número válido"
    while not dividendo:
        try:
            dividendo = ingreso_entero("Ingrese un número entero a ser dividido")
        except:
            print(mensaje_error);
    while not divisor:
        try:
            divisor = ingreso_entero(f"Ingrese un número entero que dividirá a {dividendo}")
        except:
            print(mensaje_error);
    divisionlenta = division_lenta(dividendo ,divisor)
    cociente, resto = divisionlenta
    print(f'La division entre {dividendo} y {divisor} da como resultado {cociente} y resto {resto}')
if __name__ == "__main__":
    prueba()