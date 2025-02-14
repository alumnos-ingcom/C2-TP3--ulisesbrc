################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 3. Conversión de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
from tp4ej1 import ingreso_entero_reintento
def convertir_a_fahrrenheit(centigrados):
    """
    Esta funcion convierte de centigrados a fahrenheit.
    """
    fahrenheit =(centigrados*1.8)+ 32
    return fahrenheit
def convertir_a_centigrados(fahrenheit):
    """
    Esta funcion convierte de fahrenheit a centigrados.
    """
    centigrados= (fahrenheit-32)/1.8
    return centigrados
def prueba():
    mensaje="Ingrese un número"
    cantidad_de_intentos=10
    numero = ingreso_entero_reintento(mensaje,cantidad_de_intentos)
    fahrrenheit= convertir_a_fahrrenheit(numero)
    print(f'{numero} grados son {fahrrenheit} fahrrenheit')
    centigrados=convertir_a_centigrados(numero)
    print(f'{numero} fahrrenheit son {centigrados} centigrados')
if __name__ == "__main__":
    prueba()