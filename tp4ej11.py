################
# Walter Ulises Ayllapan - @ulisesbrc
# Ejercicio 10. Palíndromo
# UNRN Andina - Introducción a la Ingenieria en Computación
################

# Reemplazar por las funciones del ejercicio
def es_palindromo(texto):
    texto_derecha_izquierda=""
    for i in texto:
        texto_derecha_izquierda = i+texto_derecha_izquierda
    return texto==texto_derecha_izquierda 
def prueba():
    texto = input("Ingrese un texto:")
    espalindromo = es_palindromo(texto)
    if espalindromo:
        print(f"El texto {texto} es palindromo")
    else:
        print(f"El texto {texto} no es palindromo")
if __name__ == "__main__":
    prueba()