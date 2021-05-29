################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 10. Factores Primos
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
def factores_primos(numero):
    factores =[]
    for n in range(2,numero):        
        if numero%n==0:
            if es_primo(n):
                factores.append(n)
    if factores:
        tupla = tuple(factores)
    else:
        if numero !=1:
            factores.append(numero)
            tupla = tuple(factores)
        else:
            tupla=()
    return tupla

if __name__ == "__main__":
   print(factores_primos(1978))