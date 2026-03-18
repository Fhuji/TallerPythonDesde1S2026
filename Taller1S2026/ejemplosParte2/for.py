

# Ejemplo1: recorrer cada letra de una palabra

'''
# Contar del 1 al 5 
for i in range(1, 6): 
print(i) 
# Iterar sobre texto 
for letra in 'Python': 
print(letra) 
# Tabla de multiplicar 
numero = int(input('¿Qué tabla quieres ver? ')) 
for i in range(1, 11): 
resultado = numero * i 
print(numero, 'x', i, '=', resultado) 

'''

# Resumen:
# Podemos usar for para iterar sobre cada carácter de un texto.
# En cada vuelta, la variable toma el siguiente carácter.

# Ejemplo2: mostrar cada letra de la palabra 'Python'

palabra = 'Python'

# for letra in palabra: asigna cada carácter a la variable 'letra'
for letra in palabra:
    print(letra)      # Muestra cada letra en una línea

'''
# Ejemplo3: mostrar la tabla de multiplicar de un número dado

numero = int(input('¿Qué tabla quieres ver? '))  # Pedimos el número

# range(1,11) genera 1,2,3,...,10
for i in range(1, 11):
    resultado = numero * i           # Multiplica el número por i
    print(numero, 'x', i, '=', resultado)   # Muestra la línea

# Resumen:
# Este código pide un número y muestra su tabla de multiplicar del 1 al 10.
# Usa un bucle for para repetir la operación 10 veces.

'''