################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 9. Números primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def es_primo(numero):
    if numero<=1:
        return False
    for n in range(2,numero):
        if numero%n==0:
            return False
    return True

if __name__ == "__main__":
   print(es_primo(79))