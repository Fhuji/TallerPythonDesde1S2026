# Ejemplo de bucle for para contar del 1 al 5
'''
# range(1,6) genera los números 1, 2, 3, 4, 5 (el 6 no se incluye)
for i in range(1, 6):
    print(i)          # Muestra cada número en una línea
'''
# Resumen:
# for se usa para repetir acciones. range(inicio, fin) crea una secuencia
# de números desde inicio hasta fin-1. El bloque dentro del for se ejecuta
# una vez por cada número.

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