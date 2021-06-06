################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 5. Números positivos y negativos
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej4 import ingrese_numero

# Reemplazar por las funciones del ejercicio
def signo(numero):
    """
    Esta función recibe un número e indica si el mismo es positivo, negativo o cero.
    """
    if(numero>0):
        return "Número positivo"
    else:
        if(numero<0):
            return "Número negativo"
        else:
            return "Número cero"

def prueba():
    numero=False
    while not numero:
        try:
            numero = ingrese_numero("Ingrese un número")
        except:
            print("El número ingresado no es válido")

    signo_numero = signo(numero)
    print(f'el {numero} es {signo_numero}')
if __name__ == "__main__":
    prueba() 