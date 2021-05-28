################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 3. Conversión de temperaturas
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio
def convertir_a_fahrrenheit(centigrados):
    """
    Esta funcion convierte de centigrados a fahrenheit.
    """
    fahrenheit =(centigrados*1.8)+ 32
    return fahrenheit;
def convertir_a_centigrados(fahrenheit):
    """
    Esta funcion convierte de fahrenheit a centigrados.
    """
    centigrados= (fahrenheit-32)/1.8
    return centigrados;


if __name__ == "__main__":
    fahrrenheit= convertir_a_fahrrenheit(39);
    print(f'39 grados son {fahrrenheit} fahrrenheit')
    centigrados=convertir_a_centigrados(22);
    print(f'22 fahrrenheit son {centigrados} centigrados')