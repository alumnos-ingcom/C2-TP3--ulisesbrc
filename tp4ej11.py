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
   print(es_palindromo("neuquen"))
if __name__ == "__main__":
    prueba()