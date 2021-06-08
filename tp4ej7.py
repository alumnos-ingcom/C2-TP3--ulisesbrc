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
    solicitar = True
    mensaje_error = "Ingrese un número válido"
    while solicitar:
        try:
            dividendo = ingreso_entero("Ingrese un número entero a ser dividido")
            solicitar=False
        except:
            print(mensaje_error)
    solicitar= True
    while solicitar:
        try:
            divisor = ingreso_entero(f"Ingrese un número entero que dividirá a {dividendo}")
            solicitar=False
        except:
            print(mensaje_error)
    divisionlenta = division_lenta(dividendo ,divisor)
    cociente, resto = divisionlenta
    print(f'La division entre {dividendo} y {divisor} da como resultado {cociente} y resto {resto}')
if __name__ == "__main__":
    prueba()