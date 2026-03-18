# Función que determina si un número es par
def es_par(numero):
    if numero % 2 == 0:      # Si el residuo al dividir por 2 es 0
        return True
    else:
        return False

# Función que clasifica un número como positivo, negativo o cero
def clasificar_numero(numero):
    if numero > 0:
        tipo = 'positivo'
    elif numero < 0:
        tipo = 'negativo'
    else:
        tipo = 'cero'
    return tipo

# Programa principal
n = int(input('Ingresa un número: '))          # Pedimos un número
print('Es par:', es_par(n))                     # Mostramos si es par
print('Clasificación:', clasificar_numero(n))   # Mostramos su tipo

# Resumen:
# Este código define dos funciones: una para saber si un número es par
# y otra para clasificarlo. Luego pide un número al usuario y muestra
# los resultados usando las funciones.