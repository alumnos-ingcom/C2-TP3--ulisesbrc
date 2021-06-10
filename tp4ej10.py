################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 10. Factores Primos
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio
from tp4ej9 import es_primo
from tp4ej1 import ingreso_entero_reintento
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

def prueba():
    cantidad_de_intentos=10
    numero = ingreso_entero_reintento("Ingrese un número",cantidad_de_intentos)
    factoresprimos = factores_primos(numero)
    mensaje=""
    for primos in factoresprimos:
        mensaje = mensaje+str(primos)+","
    cantidad_caracteres= len(mensaje)
    mensaje = mensaje[0:cantidad_caracteres-1]
    print(f"Los factores primos del numero {numero} son el {mensaje}")
if __name__ == "__main__":
    prueba()