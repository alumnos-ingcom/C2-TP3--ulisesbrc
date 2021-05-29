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
    return f"cociente {cociente}, resto {resto}"
    
if __name__ == "__main__":
   print(division_lenta( 1979 ,4))