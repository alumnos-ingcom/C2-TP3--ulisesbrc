################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 7. Restas sucesivas
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio
def division_lenta(dividendo, divisor):
    cociente = 1
    resto = dividendo - divisor
    while resto >= divisor:
        cociente = cociente +1
        resto = resto - divisor
    return (cociente,resto)
def ingrese_entero(mensaje):
    ingreso = input(mensaje + " #")
    entero= False
    while not entero:
        try:
            entero = int(ingreso)
        except ValueError as err:
            entero=ingrese_entero("Ingrese un número entero válido")
    return entero
def prueba():
    dividendo = ingrese_entero("Ingrese un número entero a ser dividido")
    divisor = ingrese_entero(f"Ingrese un número entero que dividirá a {dividendo}")
    divisionlenta = division_lenta(dividendo ,divisor)
    cociente = divisionlenta[0]
    resto = divisionlenta[1]
    print(f'La division entre {dividendo} y {divisor} da como resultado {cociente} y resto {resto}')
if __name__ == "__main__":
    prueba()